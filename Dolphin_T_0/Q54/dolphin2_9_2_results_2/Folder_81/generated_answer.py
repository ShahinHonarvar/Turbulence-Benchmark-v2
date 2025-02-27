def all_right_truncatable_prime(t):

    def is_truncatable_prime(n):
        n = str(n)
        for i in range(1, len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[98]
    primes = []
    for i in range(2, x):
        if is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)