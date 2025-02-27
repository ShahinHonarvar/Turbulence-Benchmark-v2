def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[46]
    res = []
    for num in range(x - 1, 0, -1):
        if '0' in str(num):
            continue
        trunc = num
        while trunc != 0:
            if not is_prime(trunc):
                break
            trunc //= 10
        else:
            res.append(num)
    return res