import math

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[92]
    primes = []
    if isinstance(x, int):
        n = 2
        while n < x:
            if is_prime(n) and all(is_prime((int(str(n)[:-i]) for i in range(1, len(str(n)))))):
                primes.append(n)
            n += 1
    return sorted(primes)