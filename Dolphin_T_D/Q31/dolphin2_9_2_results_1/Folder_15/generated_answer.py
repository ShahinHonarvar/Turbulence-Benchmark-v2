def if_perfect_num(l):
    if len(l) < 11:
        return False
    s = 0
    for i in range(1, l[10]):
        if l[10] % i == 0:
            s += i
    return s == l[10]