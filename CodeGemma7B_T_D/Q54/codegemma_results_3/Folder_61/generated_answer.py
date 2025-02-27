def all_right_truncatable_prime(t):
    x = t[3]
    imp = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    res = []
    for p in imp:
        n = p
        while n > 0:
            if n in imp:
                res.append(n)
            if n <= 10:
                break
            n //= 10
    return sorted(res, reverse=True) if res else []