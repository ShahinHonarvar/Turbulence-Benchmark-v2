def all_left_truncatable_prime(args):
    x = args[1]
    res = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        num = n
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    for i in range(2, x):
        if is_truncatable(i):
            res.append(i)
    res.sort(reverse=True)
    return res[:2]