def if_perfect_num(l):
    n = l[985]
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    return True