def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False
        for i in range(1, len(s)):
            if not is_prime(int(s[:-i])):
                return False
        return True
    result = [n for n in range(x + 1) if is_prime(n) and is_truncatable_prime(n)]
    return sorted(result) if result else []