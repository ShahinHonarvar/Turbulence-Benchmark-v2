def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True
    x = t[55]
    res = []
    for num in range(2, x):
        if is_prime(num):
            trunc = num
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                res.append(num)
    return sorted(res)