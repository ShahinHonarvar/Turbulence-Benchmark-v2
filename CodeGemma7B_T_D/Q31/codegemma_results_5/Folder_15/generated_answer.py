def if_perfect_num(l):
    s = l[10]
    f = s ** (1 / 2)
    if s // f == f:
        return True
    else:
        return False