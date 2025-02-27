def all_left_right_truncatable_prime(tup):
    x = tup[42]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_right_truncatable(n):
        s = str(n)
        return all((is_prime(int(s[i:])) for i in range(len(s))))
    return sorted((n for n in range(2, x + 1) if is_left_truncatable(n) and is_right_truncatable(n)))