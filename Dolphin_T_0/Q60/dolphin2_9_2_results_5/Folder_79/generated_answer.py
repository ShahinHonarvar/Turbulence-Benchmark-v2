def all_left_right_truncatable_prime(n_tuple):

    def is_prime(n):
        if n > 1:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        return False

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if str(n)[0] == '0' or str(n)[-1] == '0':
            return False
        for i in range(len(str(n)) - 1):
            if not is_prime(int(str(n)[i + 1:])) or not is_prime(int(str(n)[:-i - 1])):
                return False
        return True

    def trunc_prim_list(n):
        return [i for i in range(2, n + 1) if is_truncanable_prime(i)]
    return sorted(trunc_prim_list(n_tuple[91]))