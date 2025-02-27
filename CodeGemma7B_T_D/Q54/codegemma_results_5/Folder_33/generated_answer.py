def all_right_truncatable_prime(rythm):
    x = rhythm[945]
    g = set()

    def is_prime(n):
        if n in (1, 3, 5, 7):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n != 0:
            n //= 10
            if not is_prime(n):
                return False
        return True
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            g.add(i)
    return sorted(g, reverse=True)