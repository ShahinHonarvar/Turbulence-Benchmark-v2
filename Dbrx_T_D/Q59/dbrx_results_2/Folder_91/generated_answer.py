def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(x):
    primes = []
    for i in range(1, 10):
        if is_prime(i):
            primes.append(i)
    for i in range(1, len(str(x))):
        new_primes = []
        for j in primes:
            if is_prime(int(str(j)[i:])):
                new_primes.append(int(str(j)[i:]))
        primes = new_primes
    return sorted(primes, reverse=True)

def all_left_truncatable_prime(t):
    x = t[0]
    return left_truncatable_primes(x)