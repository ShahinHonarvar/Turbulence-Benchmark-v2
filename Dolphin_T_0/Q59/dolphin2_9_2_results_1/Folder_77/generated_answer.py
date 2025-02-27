def all_left_truncatable_prime(t):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r, w = (int(n ** 0.5), 5)
        while r * r == n:
            if n % r == 0:
                return False
            if n % w == 0:
                r = n // w
                w += 6 - 2 * (r % 2)
            else:
                w += 2 + 2 * (r % 2) - r * r % 4
                r = (r + 2) // 2
            return True

    def is_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    return list(filter(is_truncatable_prime, sorted([i for i in range(2, t[767])]))[::-1])