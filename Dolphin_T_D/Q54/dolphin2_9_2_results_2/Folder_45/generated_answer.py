def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[61]

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
        i = n
        while i > 0:
            if not is_prime(i):
                return False
            i //= 10
        return True
    return sorted([i for i in range(x) if is_right_truncatable_prime(i)])