def composite_nums_between_indices(lst):
    return {i for i in set((j for j in lst[30:88])) if j > 1 and (not any((j % k == 0 for k in range(2, j))))}