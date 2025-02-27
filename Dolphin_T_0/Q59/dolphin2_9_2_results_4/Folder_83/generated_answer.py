def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        m = int(n ** 0.5) + 1
        for x in range(3, m, 2):
            if n % x == 0:
                return False
        return True

    def truncatable_left(n):
        return all((is_prime(int(str(n)[x:])) for x in range(1, len(str(n)))))
    x = t[24]
    return sorted([n for n in range(1, x) if is_prime(n) and truncatable_left(n)])