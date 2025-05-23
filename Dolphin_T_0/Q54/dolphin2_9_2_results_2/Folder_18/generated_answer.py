def all_right_truncatable_prime(arg_tuple):
    x = arg_tuple[429]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0:
            return False
        return is_prime(n) and is_right_truncatable(n // 10)
    result = [n for n in range(x - 1, 1, -1) if is_right_truncatable(n)]
    return result