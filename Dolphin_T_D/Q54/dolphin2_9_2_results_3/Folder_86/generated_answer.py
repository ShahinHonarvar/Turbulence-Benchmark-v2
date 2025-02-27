def all_right_truncatable_prime(x):

    def is_right_truncatable_prime(num):
        n = num
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    res = []
    for i in range(x - 1, 0, -1):
        if is_right_truncatable_prime(i):
            res.append(i)
    return res