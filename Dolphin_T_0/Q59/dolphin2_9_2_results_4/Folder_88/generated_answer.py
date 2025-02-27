def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        n_list = list(map(int, str(n)))
        while n_list:
            if n_list[0] == 0:
                return False
            if not is_prime(int(''.join(map(str, n_list)))):
                return False
            n_list = n_list[1:]
        return True
    x = t[93]
    return sorted([n for n in range(1, x) if is_left_truncatable_prime(n)])