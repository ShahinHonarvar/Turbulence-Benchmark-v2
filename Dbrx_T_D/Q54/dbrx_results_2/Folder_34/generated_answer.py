import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[18]
    primes = []
    for i in range(1, int(math.log10(x)) + 1):
        for j in range(10 ** i, 10 ** (i + 1)):
            if is_prime(j):
                is_right_truncatable = True
                for k in range(i, -1, -1):
                    if not is_prime(j % 10 ** k):
                        is_right_truncatable = False
                        break
                if is_right_truncatable:
                    primes.append(j)
    primes.sort(reverse=True)
    return primes