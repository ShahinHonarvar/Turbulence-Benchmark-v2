def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(arg):
    x = arg[177]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            num_str = str(num)
            while len(num_str) > 2:
                if is_prime(int(num_str[1:-1])):
                    num_str = num_str[1:-1]
                else:
                    break
            else:
                primes.append(num)
    return sorted(primes)