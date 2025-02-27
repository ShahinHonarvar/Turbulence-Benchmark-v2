def all_left_truncatable_prime(arg):
    x = arg[70]

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n, x):
        if n > x:
            return False
        if not is_prime(n):
            return False
        s = str(n)
        while not is_prime(int(s)):
            s = s[1:]
        return is_prime(int(s)) or s == ''
    return sorted([i for i in range(1, x) if is_left_truncatable_prime(i, x)])