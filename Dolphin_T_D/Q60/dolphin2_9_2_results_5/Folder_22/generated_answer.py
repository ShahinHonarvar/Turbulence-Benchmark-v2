def all_left_right_truncatable_prime(t):
    x = t[85]

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_truncatable_prime(p):
        p_str = str(p)
        for i in range(len(p_str) - 1):
            if p_str[i] == '0':
                return False
            if not is_prime(int(p_str[i + 1:])):
                return False
        for i in range(len(p_str) - 2, -1, -1):
            if p_str[i] == '0':
                return False
            if not is_prime(int(p_str[:i])):
                return False
        return True
    ltr = [p for p in range(2, x + 1) if is_prime(p) and is_truncatable_prime(p)]
    return sorted(ltr)