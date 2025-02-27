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
        if '0' in n_str:
            return False
        for i in range(len(n_str) - 1):
            if not is_prime(int(n_str[i + 1:])) or not is_prime(int(n_str[:i + 1])):
                return False
        return True
    x = t[89]
    return sorted([n for n in range(x, 1, -1) if is_truncatable(n)], reverse=True)