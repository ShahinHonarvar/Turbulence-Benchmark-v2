def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n = str(n)
        while n:
            if n[0] == '0':
                return False
            if not is_prime(int(n)):
                return False
            n = n[1:]
        return True
    x = t[77]
    return sorted([n for n in range(x) if is_left_truncatable(n) and is_prime(n)])