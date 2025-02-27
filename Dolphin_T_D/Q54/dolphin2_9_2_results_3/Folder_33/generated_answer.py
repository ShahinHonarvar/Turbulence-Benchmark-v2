def all_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(p):
        if p < 10:
            return is_prime(p)
        if p % 10 == 0:
            return False
        if not is_prime(p):
            return False
        return is_right_truncatable(p // 10)
    result = []
    for i in range(x - 1, 0, -1):
        if is_right_truncatable(i):
            result.append(i)
    return result