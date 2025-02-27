def all_left_truncatable_prime(t):
    x = t[26]

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
        elif not str(n).isdigit() or '0' in str(n):
            return False
        else:
            return is_prime(n) and is_left_truncatable_prime(int(str(n)[1:]))
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])