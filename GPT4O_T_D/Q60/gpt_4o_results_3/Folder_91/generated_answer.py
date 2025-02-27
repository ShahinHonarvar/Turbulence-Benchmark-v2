def all_left_right_truncatable_prime(numbers):
    x = numbers[0]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(p):
        s = str(p)
        if '0' in s:
            return False
        if not is_prime(p):
            return False
        while len(s) > 2:
            s = s[1:-1]
            if not s or not is_prime(int(s)):
                return False
        return True
    result = []
    for i in range(10, x + 1):
        if is_left_right_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)