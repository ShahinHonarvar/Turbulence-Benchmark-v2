def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            n = n // 10
            if n < 10 or not is_prime(n):
                return False
        return True

    def is_right_truncatable(n):
        s = str(n)
        while len(s) > 0:
            s = s[:-1]
            if len(s) < 2 or not is_prime(int(s)):
                return False
        return True
    x = t[0]
    result = []
    for num in range(x, 1, -1):
        if '0' not in str(num) and is_prime(num) and is_left_truncatable(num) and is_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)