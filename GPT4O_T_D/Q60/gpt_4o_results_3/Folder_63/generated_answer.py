def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            left_trunc = int(s[i:])
            right_trunc = int(s[:len(s) - i])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                return False
        return True
    x = numbers[88]
    results = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return results