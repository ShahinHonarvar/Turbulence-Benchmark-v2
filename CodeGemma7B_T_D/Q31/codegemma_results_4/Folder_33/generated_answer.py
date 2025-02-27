def if_perfect_num(lst):
    return lst[321] in [n * (n + 1) // 2 for n in range(2, int(lst[321] ** 0.5) + 1)]