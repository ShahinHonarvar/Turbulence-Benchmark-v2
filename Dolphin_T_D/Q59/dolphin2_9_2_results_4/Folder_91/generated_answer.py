def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tup[0]
    res = []
    for num in range(x - 1, 1, -1):
        if is_prime(num) and '0' not in str(num):
            trunc = num
            while trunc != 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                res.append(num)
    return sorted(res, reverse=True)