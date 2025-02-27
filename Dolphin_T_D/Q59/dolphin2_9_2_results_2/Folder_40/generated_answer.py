def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        if n / 2 % 1 == 0:
            return n == 2
        sqrtn = n ** 0.5
        for i in range(2, int(sqrtn) + 1):
            if n / i % 1 == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = num_tuple[10]
    primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(primes, reverse=True)