def all_left_right_truncatable_prime(numbers_tuple):

    def check_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_truncatable(n):
        if n < 10:
            return n != 0 and check_prime(n)
        return n % 10 != 0 and check_prime(n) and check_truncatable(n // 10) and check_truncatable(n // 10 % 10 * 10 + n % 10)
    x = numbers_tuple[992]
    return sorted([i for i in range(2, x + 1) if check_truncatable(i)])