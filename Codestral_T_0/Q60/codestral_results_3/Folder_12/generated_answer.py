def all_left_right_truncatable_prime(t):
    x = t[70]

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
            n //= 10
        return True

    def is_right_truncatable(n):
        s = str(n)
        while len(s) > 0:
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return True
    result = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_left_truncatable(i) and is_right_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)