def all_left_truncatable_prime(test_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_truncatable(n):
        if n <= 1 or '0' in str(n):
            return False
        if is_prime(n):
            return True
        return False
    x = test_tuple[618]
    return [i for i in range(2, x) if check_truncatable(i) and check_truncatable(int(str(i)[:-1]))]