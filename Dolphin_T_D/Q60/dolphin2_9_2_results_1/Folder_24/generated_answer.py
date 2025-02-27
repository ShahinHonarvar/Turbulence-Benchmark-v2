def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n ** 0.5)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[65]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            for d in range(1, 9):
                if num // 10 ** d % 10 == 0:
                    break
                if is_prime(num // 10 ** d) and is_prime(num % 10 ** d):
                    primes.append(num)
    return sorted(primes, reverse=True)