def all_right_truncatable_prime(x):

    def check_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_truncatable(n):
        if check_prime(n):
            n = n // 10
            while n:
                if not check_prime(n):
                    return False
                n = n // 10
            return True
        return False
    res = []
    for i in range(2, int(x)):
        if check_truncatable(i):
            res.append(i)
    return sorted(res)