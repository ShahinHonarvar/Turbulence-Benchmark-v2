def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[19]
    truncatable_primes = []
    for n in range(10, x + 1):
        if '0' not in str(n) and is_prime(n):
            num_str = str(n)
            is_truncatable = True
            for i in range(len(num_str)):
                truncated_num = int(num_str[i:-i or None])
                if not is_prime(truncated_num):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(n)
    return sorted(truncatable_primes)