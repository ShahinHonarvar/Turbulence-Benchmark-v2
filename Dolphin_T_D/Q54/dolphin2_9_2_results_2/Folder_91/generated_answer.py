import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(x):
    primes = []
    for i in range(2, x):
        if is_prime(i):
            trunc_i = i
            while trunc_i != 0 and is_prime(trunc_i):
                trunc_i //= 10
            if trunc_i == 0:
                primes.append(i)
    return sorted(primes, reverse=True)