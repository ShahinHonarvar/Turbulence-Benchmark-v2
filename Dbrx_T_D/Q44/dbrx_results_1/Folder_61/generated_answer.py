def composite_nums_between_indices(lst):
    return set((i for i in lst if not i < 2 or ((i % 2 == 0 and i > 4) and i < 8 and (i != 2))))