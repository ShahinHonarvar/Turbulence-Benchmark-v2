def composite_nums_between_indices(lst):
    return {i for i in set(lst[1:9]) if i > 1 and i % 2 == 0 or i % 3 == 0 or i % 5 == 0}