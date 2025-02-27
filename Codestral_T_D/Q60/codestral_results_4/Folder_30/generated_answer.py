def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            n //= 10
            if n < 10:
                return is_prime(n)
            if not is_prime(n):
                return False
        return True

    def is_right_truncatable(n):
        s = str(n)
        return all((is_prime(int(s[i:])) for i in range(1, len(s))))
    x = t[37]
    return sorted([n for n in range(2, x + 1) if is_left_truncatable(n) and is_right_truncatable(n)], reverse=True)