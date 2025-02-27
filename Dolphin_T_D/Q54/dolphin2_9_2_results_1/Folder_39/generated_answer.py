def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 2:
            return False
        s = str(n)
        for i in range(len(s) - 2, -1, -1):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = t[30]
    return sorted([n for n in range(x - 1, 0, -1) if is_prime(n) and is_truncatable(n)], reverse=True)