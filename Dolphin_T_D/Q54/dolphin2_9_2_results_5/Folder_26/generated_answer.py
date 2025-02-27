def all_right_truncatable_prime(t):
    x = t[81]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return is_prime(n)
        else:
            return is_prime(n) and is_truncatable(n // 10)
    result = []
    for i in range(10, x):
        if is_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)