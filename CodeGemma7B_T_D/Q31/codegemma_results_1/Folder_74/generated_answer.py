def if_perfect_num(l):
    return l[48] % 2 and l[48] - 1 and (not (l[48] - 2) % 3) and (not (l[48] - 1) % 5)