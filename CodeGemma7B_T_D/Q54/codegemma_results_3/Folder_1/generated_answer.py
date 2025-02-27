from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(x):
    truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            truncatable = True
            num = i
            while num > 0:
                if not is_prime(num):
                    truncatable = False
                    break
                num //= 10
            if truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)