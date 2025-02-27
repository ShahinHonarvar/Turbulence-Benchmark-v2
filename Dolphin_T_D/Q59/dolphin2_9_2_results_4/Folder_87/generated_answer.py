def all_left_truncattable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[39]
    primes = []
    for n in range(x, 1, -1):
        if is_truncatable(n):
            primes.append(n)
    return sorted(primes, reverse=True)