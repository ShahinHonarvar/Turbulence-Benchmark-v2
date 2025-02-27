def all_left_truncatable_prime(t):
    x = t[14]

    def truncate(num):
        s = str(num)
        return [int(s[:i]) for i in range(1, len(s))]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        return is_prime(n) and all((is_prime(x) for x in truncate(n)))
    return sorted([n for n in range(2, x) if '0' not in str(n) and is_left_truncatable_prime(n)])