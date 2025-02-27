def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 2:
            return False
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[975]
    primes = []
    for i in range(x - 1, 0, -1):
        if is_right_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True)