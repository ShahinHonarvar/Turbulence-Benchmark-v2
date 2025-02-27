from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(n):
    primes = set([i for i in range(2, n) if is_prime(i)])
    rt_primes = set()
    for p in primes:
        k = p
        while k > 0:
            if k in primes and (k <= 9 or (k % 10 != 2 and k % 10 != 5)):
                rt_primes.add(k)
            k //= 10
    return sorted(rt_primes)