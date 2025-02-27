def all_left_right_truncatable_prime(bound_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[:-1])
        return True

    def is_left_right_truncatable_prime(n):
        return is_left_truncatable_prime(n) and is_right_truncatable_prime(n)
    x = bound_tuple[8]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_right_truncatable_primes = [i for i in primes if is_left_right_truncatable_prime(i)]
    return sorted(left_right_truncatable_primes, reverse=True)