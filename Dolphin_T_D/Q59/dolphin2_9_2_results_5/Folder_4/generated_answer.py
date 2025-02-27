def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if n == 0:
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[96]
    primes = []
    for n in range(x, 1, -1):
        if is_left_truncatable(n):
            primes.append(n)
    return sorted(primes, reverse=True)