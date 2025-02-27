def all_left_truncatable_prime(t):
    x = t[55]

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n == 2:
            return True
        if n == 1 or n % 2 == 0 or '0' in str(n):
            return False
        str_n = str(n)
        for i in range(len(str_n) - 1, 0, -1):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)])