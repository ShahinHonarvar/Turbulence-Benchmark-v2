from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[6]
    truncatable_primes = []
    for i in range(9, x):
        if is_prime(i):
            num = i
            while num > 0:
                if not is_prime(num):
                    break
                truncatable_primes.append(num)
                num = num // 10
    return sorted(truncatable_primes, reverse=True)