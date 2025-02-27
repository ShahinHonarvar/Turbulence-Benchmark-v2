def all_left_right_truncatable_prime(int_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n <= 9:
            return is_prime(n)
        while n > 9:
            if not is_prime(n):
                return False
            n = n // 10
        return is_prime(n)
    x = int_tuple[19]
    res = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            res.append(i)
    res.sort()
    return res