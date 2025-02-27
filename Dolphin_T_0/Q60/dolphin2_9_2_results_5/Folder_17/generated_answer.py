def all_left_right_truncatable_prime(t):
    x = t[36]

    def is_truncatable(n):
        if n < 10:
            return True
        if str(n)[-1] == '0':
            return False
        return is_prime(n) and is_truncatable(n // 10) and is_truncatable(int(str(n)[1:-1]))

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([i for i in range(2, x + 1) if is_truncatable(i)], reverse=True)