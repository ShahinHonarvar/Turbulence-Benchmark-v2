def composite_nums_between_indices(lst):
    return set((x for i, x in enumerate(lst) if i in range(27, 56) and all((x % j for j in range(2, int(x ** 0.5) + 1))) != 0))