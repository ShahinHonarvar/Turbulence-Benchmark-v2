def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        return all((is_prime(int(s[i:])) and is_prime(int(s[:i])) for i in range(1, len(s))))
    return sorted([i for i in range(2, t[39] + 1) if is_left_right_truncatable_prime(i)])