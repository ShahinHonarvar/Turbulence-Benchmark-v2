def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    def is_right_truncatable(n):
        s = str(n)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return True
    x = numbers[88]
    result = []
    for n in range(2, x + 1):
        if '0' not in str(n) and is_left_truncatable(n) and is_right_truncatable(n):
            result.append(n)
    return sorted(result)