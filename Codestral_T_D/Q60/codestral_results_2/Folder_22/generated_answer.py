def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True

    def is_left_right_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        return all((is_prime(int(s[i:])) and is_prime(int(s[:-i])) for i in range(1, len(s))))
    x = t[85]
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable(n)])