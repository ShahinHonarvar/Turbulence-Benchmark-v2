def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if '0' in s[i:] or '0' in s[:i + 1]:
                continue
            if not (is_prime(int(s[i:])) and is_prime(int(s[:i + 1]))):
                return False
        return True
    x = numbers[86]
    return sorted([n for n in range(2, x + 1) if is_prime(n) and is_truncatable(n)])