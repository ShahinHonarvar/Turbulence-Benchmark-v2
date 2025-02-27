def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(p):
        if not is_prime(p):
            return False
        p = str(p)
        while len(p) > 1:
            p = p[1:]
            if not is_prime(int(p)):
                return False
        return True
    x = t[74]
    result = []
    for i in range(2, x):
        if is_truncatable(i):
            result.append(i)
    return sorted(result)