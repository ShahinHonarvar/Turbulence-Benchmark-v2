def all_left_right_truncatable_prime(t):
    x = t[41]

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        while len(str(n)) > 1:
            if not is_prime(n):
                return False
            n = int(str(n)[1:-1])
        return is_prime(n)
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable(n)])