def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        while len(str_n) > 1:
            str_n = str_n[1:]
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[:-1]
            if not is_prime(int(str_n)):
                return False
        return True
    x = t[41]
    return sorted([i for i in range(2, x + 1) if is_prime(i) and is_truncatable(i)])