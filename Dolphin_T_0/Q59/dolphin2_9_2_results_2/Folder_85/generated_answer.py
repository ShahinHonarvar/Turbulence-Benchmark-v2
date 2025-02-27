def all_left_truncatable_prime(t):
    x = t[94]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        a = n
        while a:
            if a == 0 or not is_prime(a):
                return False
            a = a // 10
        return True
    return sorted([n for n in range(2, x) if is_left_truncatable(n)])