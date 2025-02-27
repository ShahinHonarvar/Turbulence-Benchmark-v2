def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_left_truncatable_prime(t):
    x = t[466]
    primes = [2, 3, 5, 7]
    for p in range(11, x, 2):
        if is_prime(p) and all((is_prime(int(str(p)[i:])) for i in range(1, len(str(p))))):
            primes.append(p)
    return sorted(primes, reverse=True)