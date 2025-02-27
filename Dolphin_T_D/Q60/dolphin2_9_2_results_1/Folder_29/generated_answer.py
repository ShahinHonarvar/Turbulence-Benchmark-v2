def all_left_right_truncatable_prime(t):
    x = t[55]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        while n != 0 and n != 1:
            n = int(str(n)[1:-1])
            if not is_prime(n):
                return False
        return True
    return [n for n in range(x, 1, -1) if is_truncatable(n)]