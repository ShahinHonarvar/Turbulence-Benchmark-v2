def all_left_right_truncatable_prime(t):
    x = t[77]

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            if s[0] == '0' or s[-1] == '0':
                return False
            if not is_prime(int(s)):
                return False
            s = s[1:-1]
        return is_prime(int(s))
    return sorted([n for n in range(x, 1, -1) if is_left_right_truncatable_prime(n)], reverse=True)