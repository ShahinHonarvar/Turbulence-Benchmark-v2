def all_left_right_truncatable_prime(x):

    def is_left_right_truncatable(n):

        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        if str(n)[0] == '0' or str(n)[-1] == '0':
            return False
        while len(str(n)) > 1:
            n = n // 10
            if not is_prime(n):
                return False
        return True
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable(n) and is_prime(n)])