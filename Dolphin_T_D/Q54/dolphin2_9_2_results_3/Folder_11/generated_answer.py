def all_right_truncatable_prime(t):
    x = t[86]

    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if is_prime(n):
            n = str(n)
            for i in range(1, len(n)):
                if not is_prime(int(n[i:])):
                    return False
            return True
        return False
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])