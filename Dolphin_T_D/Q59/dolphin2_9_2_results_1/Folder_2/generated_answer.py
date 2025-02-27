def all_left_truncatable_prime(positive_integer_tuple):
    x = positive_integer_tuple[618]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_no_0(n):
        while n:
            if n % 10 == 0:
                return False
            n //= 10
        return True

    def is_left_truncatable_prime(n):
        while n > 1:
            if not is_no_0(n):
                return False
            if not is_prime(n):
                return False
            n //= 10
        return True
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n) and is_prime(n)])