def all_left_truncatable_prime(t):
    x = t[31]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if n < 10:
            return is_prime(n)
        return is_prime(n) and is_left_truncatable(n // 10)
    result = []
    for i in range(x, 0, -1):
        if is_left_truncatable(i):
            result.append(i)
    return result[::-1]