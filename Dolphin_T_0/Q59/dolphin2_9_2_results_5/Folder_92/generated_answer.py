def all_left_truncatable_prime(t):
    x = t[7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if n_str[i] == '0':
                return False
            if not is_prime(int(n_str[i:])):
                return False
        return True
    return sorted([n for n in range(2, x) if is_left_truncatable(n)])