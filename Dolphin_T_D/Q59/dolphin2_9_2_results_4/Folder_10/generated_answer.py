def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        left = n
        while left > 0:
            if not is_prime(left):
                return False
            left //= 10
        return True
    x = tup[38]
    res = [i for i in range(x, 0, -1) if is_truncatable(i)]
    return res