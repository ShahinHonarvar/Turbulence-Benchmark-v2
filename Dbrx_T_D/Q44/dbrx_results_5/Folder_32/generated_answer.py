def composite_nums_between_indices(lst):
    indices = set(range(10, 67))
    composite_numbers = {i for i in lst if i > 1 and i % 2 == 0}
    return composite_numbers & indices