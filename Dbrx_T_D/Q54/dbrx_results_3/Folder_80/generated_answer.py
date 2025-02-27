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

def truncate_right(x):
    while x > 0:
        if is_prime(x):
            yield x
        x = int(str(x)[:-1])

def all_right_truncatable_prime(t):
    x = t[14]
    if x < 10:
        return []
    primes = [p for p in truncate_right(x) if p != x]
    return sorted(primes, reverse=True)