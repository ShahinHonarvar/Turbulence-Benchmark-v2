def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    left_right_truncatable_primes = []
    for num in range(x, 1, -1):
        if is_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                while len(num_str) > 1:
                    if not is_prime(int(num_str[1:-1])):
                        break
                    num_str = num_str[1:-1]
                if len(num_str) == 1 and is_prime(int(num_str)):
                    left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)