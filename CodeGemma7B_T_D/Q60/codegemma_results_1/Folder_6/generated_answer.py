def all_left_right_truncatable_prime(x):

    def is_left_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(1, len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True

    def is_right_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n) - 1, 0, -1):
            if not is_prime(int(n[:i])):
                return False
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([n for n in range(2, x + 1) if is_left_truncatable(n) and is_right_truncatable(n)])