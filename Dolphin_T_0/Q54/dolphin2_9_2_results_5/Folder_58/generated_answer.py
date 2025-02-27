def all_right_truncatable_prime(tup):

    def is_prime(n):
        if n in (2, 3) or n % 2 == 0:
            return n in (2, 3)
        if n % 3 == 0 or n % 5 == 0:
            return False
        i, w = (5, 2)
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def is_truncatable_right(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = tup[975]
    return sorted([n for n in range(x - 1, 1, -1) if is_truncatable_right(n)], reverse=True)