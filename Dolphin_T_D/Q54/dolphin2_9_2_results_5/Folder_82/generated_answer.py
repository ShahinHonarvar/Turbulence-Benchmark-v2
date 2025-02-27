def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 10:
            return is_prime(n)
        if not is_prime(n):
            return False
        return is_right_truncatable(n // 10)
    x = t[69]
    primes = [i for i in range(2, x) if is_right_truncatable(i)]
    return sorted(primes, reverse=True)