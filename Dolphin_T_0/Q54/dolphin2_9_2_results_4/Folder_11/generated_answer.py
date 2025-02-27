def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[86]
    res = []
    for i in range(1, x):
        if is_prime(i):
            trunc = i
            while trunc > 1:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                res.append(i)
    return sorted(res)