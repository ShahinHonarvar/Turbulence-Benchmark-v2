def all_left_right_truncatable_prime(n_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(n ** 0.5)
        for i in range(3, sqrt_n + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        while len(str_n) > 1:
            if not is_prime(int(str_n[1:])) or not is_prime(int(str_n[:-1])):
                return False
            str_n = str_n[1:-1]
        return True
    x = n_tuple[85]
    return sorted(set([n for n in range(2, x + 1) if is_truncatable_prime(n)]))