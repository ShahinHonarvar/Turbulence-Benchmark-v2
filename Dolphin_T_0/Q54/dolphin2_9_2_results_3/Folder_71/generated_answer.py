def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if n in primes:
                yield n
            n //= 10
    x = t[22]
    primes = [i for i in range(x) if is_prime(i)]
    rtps = list(is_right_truncatable_prime(x - 1))
    return sorted(rtps, reverse=True)