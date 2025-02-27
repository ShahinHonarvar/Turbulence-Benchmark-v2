def all_left_right_truncatable_prime(t):
    x = t[52]

    def is_trunc_prime(n):
        if n < 2:
            return False
        if '0' in str(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([n for n in range(2, x + 1) if is_trunc_prime(n)], reverse=True)