def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(p):
        for i in range(1, len(str(p))):
            if not is_prime(int(str(p)[i:])) or not is_prime(int(str(p)[:-i])):
                return False
        return True
    x = t[803]
    return sorted([p for p in range(2, x + 1) if '0' not in str(p) and is_prime(p) and is_truncatable(p)])