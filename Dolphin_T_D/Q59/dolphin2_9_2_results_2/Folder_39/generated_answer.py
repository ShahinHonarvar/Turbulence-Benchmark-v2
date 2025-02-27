def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 1:
            if n % 10 == 0:
                return False
            m = n
            while m > 0 and m % 10 != 0:
                m //= 10
            if not is_prime(m):
                return False
            n //= 10
        return True
    x = t[30]
    primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(primes, reverse=True)