def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(p):
        while p > 0:
            if not is_prime(p):
                return False
            p //= 10
        return True
    x = t[55]
    ret = [i for i in range(2, x) if is_prime(i) and is_left_truncatable(i)]
    return sorted(ret)