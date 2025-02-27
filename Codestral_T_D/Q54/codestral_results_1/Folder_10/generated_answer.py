def all_right_truncatable_prime(t):
    x = t[38]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    return sorted([n for n in range(x - 1, 1, -1) if right_truncatable(n)], reverse=True)