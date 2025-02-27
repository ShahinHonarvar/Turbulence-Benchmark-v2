def all_right_truncatable_prime(tup):
    num = tup[945]
    res = []
    for d in reversed(range(1, num)):
        n = d
        while n > 0:
            if n % 10 != 0 and n % 2 != 0 and (n not in [3, 5, 7, 9]):
                m = n
                while m >= 10:
                    m //= 10
                if m ** 3 % 4 == 3 and m not in res:
                    res.append(m)
            n //= 10
    if res:
        return sorted(res, reverse=True)
    return []