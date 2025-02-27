def composite_nums_between_indices(lst):
    return set((i for i in lst[35:50] if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))))