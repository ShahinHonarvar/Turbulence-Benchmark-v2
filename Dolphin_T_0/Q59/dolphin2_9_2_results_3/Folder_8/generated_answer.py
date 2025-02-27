def all_left_truncatable_prime(L):
    x = L[41]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        else:
            return is_prime(n) and is_left_truncatable_prime(n // 10)
    res = [n for n in range(x - 1, 1, -1) if is_left_truncatable_prime(n)]
    return res