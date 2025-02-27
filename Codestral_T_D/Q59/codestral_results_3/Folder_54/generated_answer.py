def all_left_truncatable_prime(t):
    x = t[88]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        elif not is_prime(n):
            return False
        elif '0' in str(n):
            return False
        else:
            return is_left_truncatable_prime(int(str(n)[1:]))
    return sorted([n for n in range(x - 1, 1, -1) if is_left_truncatable_prime(n)])