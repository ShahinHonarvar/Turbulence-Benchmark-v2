import math

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[10]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j != 0:
                j //= 10
                if not is_prime(j):
                    break
            else:
                primes.append(i)
    primes.sort(reverse=True)
    return primes