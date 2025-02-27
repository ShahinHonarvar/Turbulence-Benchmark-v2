def all_right_truncatable_prime(x: int) -> list:

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n: int) -> bool:
        while n > 9:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return is_prime(n)
    return sorted(filter(is_right_truncatable_prime, range(1, x)))