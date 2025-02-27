def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n < 2:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True

    def is_truncatable(n):
        n_str = str(n)
        for _ in range(len(n_str) - 1):
            if not is_prime(int(n_str[1:])) or not is_prime(int(n_str[:-1])):
                return False
            n_str = n_str[1:-1]
        return True
    return [n for n in range(2, x + 1) if is_prime(n) and is_truncatable(n)]