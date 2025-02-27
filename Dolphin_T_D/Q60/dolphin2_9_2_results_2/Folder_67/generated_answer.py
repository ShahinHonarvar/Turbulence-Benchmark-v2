def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n_str = str(n)
        while n_str:
            if not n_str[0] and n_str[-1]:
                n_str = n_str[1:-1]
            else:
                return False
            if not is_prime(int(n_str)):
                return False
        return True
    x = t[71]
    return list(filter(is_truncatable, reversed(range(2, x + 1))))