def all_left_right_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        return all((is_prime(n) and is_prime(n // 10) and is_prime(n % 10) for n in range(n, 10, -1)))
    x = tup[784]
    primes = [n for n in range(2, x + 1) if is_prime(n) and is_truncatable(n)]
    return sorted(primes)