def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        num = n
        while n > 0:
            n //= 10
            if not is_prime(num):
                return False
            num //= 10
        return True
    x = t[3]
    primes = [i for i in range(2, x) if is_prime(i) and is_right_truncatable(i)]
    return sorted(primes, reverse=True)