def all_left_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        while len(str_n) > 1:
            if len(str_n) == 2 or is_prime(int(str_n)):
                str_n_left = str_n[:1] + str_n[2:]
                str_n_right = str_n[1:-1]
                if str_n_left == '' or str_n_right == '':
                    return False
                if not is_prime(int(str_n_left)) or not is_prime(int(str_n_right)):
                    return False
            else:
                return False
            str_n = str_n_left
        return True
    x = num_tuple[803]
    return sorted([i for i in range(2, x + 1) if is_truncatable(i) and is_prime(i)])