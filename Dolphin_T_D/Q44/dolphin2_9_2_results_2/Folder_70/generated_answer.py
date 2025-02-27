def composite_nums_between_indices(lst):
    return set((i for i in lst[32:36] if len([x for x in range(2, i // 2 + 1) if i % x == 0]) > 0))