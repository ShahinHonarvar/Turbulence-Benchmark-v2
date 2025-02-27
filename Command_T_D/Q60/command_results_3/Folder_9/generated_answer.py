def all_left_right_truncatable_prime(test_case):

    def is_left_right_truncatable_prime(n):
        if n < 2 or n == 2 or n == 3 or (n == 5):
            return True
        if n % 2 == 0 or n % 5 == 0:
            return False
        if n % 2 == 0 or n % 5 == 0:
            return False
        return True
    return [n for n in range(test_case[29]) if is_left_right_truncatable_prime(n)]