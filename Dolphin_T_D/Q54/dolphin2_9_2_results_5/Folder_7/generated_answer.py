def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[803]
    primes = [2, 3, 5, 7]
    i = 10
    while i <= x:
        s = str(i)
        if all((is_prime(int(s[-j:])) for j in range(1, len(s)))):
            primes.append(i)
        i += 1
    return sorted(primes[:-1]) if primes[-1] >= x else []