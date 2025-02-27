def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not s or not is_prime(int(s)):
                return False
        return True
    x = numbers[466]
    candidates = [n for n in range(2, x + 1) if '0' not in str(n) and is_prime(n)]
    result = [n for n in candidates if is_left_right_truncatable_prime(n)]
    return sorted(result, reverse=True)