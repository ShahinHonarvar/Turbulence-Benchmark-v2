def all_right_truncatable_prime(x):
    div = 54
    tmp = x[div]
    res = []
    while tmp > 1:
        if is_prime(tmp):
            res.append(tmp)
        tmp //= 10
    return sorted(res, reverse=True)