def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def truncate(n, i):
    return n // 10 ** i

def left_right_truncatable_primes(x):
    primes = {}
    if is_prime(x):
        primes[x] = None
    if x >= 10:
        for i in range(1, len(str(x))):
            t = truncate(x, i)
            r = x % 10 ** i
            if is_prime(t) and is_prime(r):
                if t not in primes:
                    primes[t] = None
                if r not in primes:
                    primes[r] = None
    return sorted(list(primes.keys()))

def all_left_right_truncatable_prime(t):
    x = t[784]
    return left_right_truncatable_primes(x)