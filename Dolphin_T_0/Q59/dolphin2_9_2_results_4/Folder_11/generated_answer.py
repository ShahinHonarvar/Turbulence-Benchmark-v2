def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    x = tup[86]
    return sorted([i for i in range(2, x) if is_left_truncatable(i) and is_prime(i)])