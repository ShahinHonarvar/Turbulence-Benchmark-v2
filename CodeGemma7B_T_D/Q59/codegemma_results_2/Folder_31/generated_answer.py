def all_left_truncatable_prime(t):
    x = t[50]

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable_prime(n):
        if not is_prime(n):
            return []
        result = []
        for i in range(1, n):
            if n % i == 0 and is_prime(n // i):
                result.append(n // i)
        return result
    result = []
    for i in range(2, x):
        if is_prime(i):
            tmp = left_truncatable_prime(i)
            if not any((j in tmp for j in result)):
                result.append(i)
    return sorted(result, reverse=True)