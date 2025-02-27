def all_left_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0:
            return False
        for last_digit in range(1, 10):
            if is_prime(n // 10 * last_digit + n % 10):
                return True
        return False
    x = num_tuple[39]
    return [n for n in range(x, 1, -1) if is_left_right_truncatable(n) and all((is_prime(n // 10 ** i * last_digit + n % 10 ** i) for i in range(1, len(str(n)) // 2 + 1) for last_digit in range(10)))]