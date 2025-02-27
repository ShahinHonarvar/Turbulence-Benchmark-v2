def all_right_truncatable_prime(bound_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True
    x = bound_tuple[35]
    primes = [i for i in range(1, x) if is_right_truncatable_prime(i)]
    return sorted(primes, reverse=True)