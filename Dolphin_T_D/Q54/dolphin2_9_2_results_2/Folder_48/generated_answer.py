def all_right_truncatable_prime(tuple_of_positive_integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** (1 / 2)) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = tuple_of_positive_integers[835]
    right_truncatable_primes = [n for n in range(2, x) if is_prime(n) and is_truncatable(n)]
    return sorted(right_truncatable_primes)