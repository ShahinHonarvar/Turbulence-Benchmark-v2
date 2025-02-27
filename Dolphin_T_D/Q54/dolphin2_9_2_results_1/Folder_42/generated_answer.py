def is_prime(n):
    if n in (1, 2):
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[64]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            if all((is_prime(int(str(i)[-j:])) for j in range(1, len(str(i)) + 1))):
                primes.append(i)
    return sorted(primes, reverse=True)