def all_left_truncatable_prime(int_tuple):
    x = int_tuple[71]

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    result = [n for n in range(x - 1, 1, -1) if is_truncatable(n) and is_prime(n)]
    return result