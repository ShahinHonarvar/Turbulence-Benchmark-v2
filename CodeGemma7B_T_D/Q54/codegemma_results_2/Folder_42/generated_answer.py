def all_right_truncatable_prime(tup):
    x = tup[64]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        for i in range(1, n + 1):
            digit = n % 10
            n //= 10
            if not is_prime(digit):
                return False
        return is_prime(n)
    result = []
    for i in range(2, x):
        if is_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True) or []