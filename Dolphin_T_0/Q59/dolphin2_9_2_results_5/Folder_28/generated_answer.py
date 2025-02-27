def all_left_truncatable_prime(t):

    def is_truncatable(n, primes):
        if n < 2:
            return False
        for p in primes:
            if n % p == 0:
                return False
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [2]
    n = 3
    while n < t[19]:
        if is_prime(n):
            if is_truncatable(n, primes):
                primes.append(n)
        n += 2
    return primes