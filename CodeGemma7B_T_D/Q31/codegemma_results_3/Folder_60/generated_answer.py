def if_perfect_num(lst):
    return lst[88] in [i * i for i in range(1, int(lst[88] ** 0.5) + 1)]