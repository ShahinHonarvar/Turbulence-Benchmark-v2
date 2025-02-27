def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2 or '0' in str(n):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        return all((is_prime(int(s[i:])) and is_prime(int(s[:-i])) for i in range(1, len(s))))
    return sorted(filter(is_truncatable, range(2, t[3] + 1)), reverse=True)