def all_left_truncatable_prime(p):

    def is_left_truncatable_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return is_left_truncatable(n)

    def is_left_truncatable(n):
        if n == 2:
            return True
        if n < 2 or n % 10 == 0:
            return False
        return is_left_truncatable(n // 10)
    x = p[835]
    return [i for i in range(2, x) if is_left_truncatable_prime(i)]