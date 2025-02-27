def all_right_truncatable_prime(t):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n < 2 or n % 2 == 0:
            return False
        sq = int(n ** 0.5)
        for i in range(3, sq + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 10:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[433]
    primes = []
    for n in range(x, 1, -1):
        if is_right_truncatable(n):
            primes.append(n)
    return sorted(primes, reverse=True)