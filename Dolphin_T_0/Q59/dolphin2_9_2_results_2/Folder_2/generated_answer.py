def all_left_truncatable_prime(t):

    def _is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def _is_left_truncatable_prime(n):
        for xn in str(n)[::-1]:
            if xn == '0':
                return False
            if not _is_prime(int(xn)):
                return False
        return True
    x = t[618]
    return sorted([i for i in range(2, x) if _is_left_truncatable_prime(i)])