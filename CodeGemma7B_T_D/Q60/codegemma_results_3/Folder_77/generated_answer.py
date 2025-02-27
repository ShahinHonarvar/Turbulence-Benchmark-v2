def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_prime(n):
        while n > 1:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def left_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and left_truncatable_prime(i) and right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)