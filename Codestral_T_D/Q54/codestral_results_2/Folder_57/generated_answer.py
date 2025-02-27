def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n //= 10
            if not is_prime(n):
                return False
        return True
    x = num_tuple[54]
    right_truncatable_primes = [n for n in range(x - 1, 1, -1) if is_right_truncatable_prime(n)]
    return right_truncatable_primes