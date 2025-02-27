def all_left_truncatable_prime(n):
    res = []
    for i in range(1, n[0] + 1):
        if all((str(j) for j in range(i, n[0] + 1, i))):
            res.append(i)
    return res