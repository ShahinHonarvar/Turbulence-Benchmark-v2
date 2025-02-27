import math

def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    d = 3
    while d <= r + 1:
        if n % d == 0:
            return False
        d += 2
    return True

def all_right_truncatable_prime(t):
    x = t[42]
    primes = []
    for n in range(2, x):
        if is_prime(n):
            trunc = n
            while trunc > 0:
                trunc = int(trunc / 10)
                if not is_prime(trunc):
                    break
                else:
                    primes.append(n)
                    break
    return sorted(primes)