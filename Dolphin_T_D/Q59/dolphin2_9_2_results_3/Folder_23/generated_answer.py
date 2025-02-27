def all_left_truncatable_prime(t):

    def _is_left_truncatable_prime(n):
        if n < 2 or n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return _is_left_truncatable_prime(n // 10) if n > 9 else True
    x = t[76]
    return sorted([n for n in reversed(range(x)) if _is_left_truncatable_prime(n)], reverse=False)