def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[97]

    def is_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0 or not is_prime(n):
            return False
        return is_right_truncatable_prime(n // 10)
    return sorted([n for n in range(2, x) if is_right_truncatable_prime(n)])