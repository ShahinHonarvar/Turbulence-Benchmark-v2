def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(p):
        if not is_prime(p):
            return False
        if p == 0:
            return False
        return is_truncatable(p // 10)
    result = []
    num = t[126]
    for i in range(num - 1, 0, -1):
        if is_truncatable(i):
            result.append(i)
    return result