def all_right_truncatable_prime(tup):
    x = tup[86]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(len(s) - 1, 0, -1):
            if not is_prime(int(s[i:])):
                return False
        return True
    return sorted(list(filter(is_truncatable_prime, range(2, x))))