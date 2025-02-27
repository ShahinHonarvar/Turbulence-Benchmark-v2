def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        s = n
        while s > 0:
            if not is_prime(s):
                return False
            s //= 10
        return True
    x = t[65]
    result = []
    for i in range(x - 1, 0, -1):
        if is_right_truncatable_prime(i):
            result.append(i)
    return result