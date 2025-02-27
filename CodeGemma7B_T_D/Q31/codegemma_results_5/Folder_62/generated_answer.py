def if_perfect_num(l):
    return True if l[926] % sum([j for j in range(1, l[926]) if l[926] % j == 0]) == 0 else False