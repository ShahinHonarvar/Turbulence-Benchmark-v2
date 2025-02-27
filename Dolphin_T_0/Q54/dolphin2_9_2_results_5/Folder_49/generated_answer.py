def all_right_truncatable_prime(tup):
    x = tup[14]

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        sqr = int(n ** 0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if n in (2, 3):
            return True
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])