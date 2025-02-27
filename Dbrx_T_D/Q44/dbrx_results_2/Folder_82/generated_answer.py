def composite_nums_between_indices(lst):
    composite_nums = {i for i in lst[30:31] if i > 1 and (not all((i % j for j in range(2, int(i ** 0.5) + 1))))}
    return composite_nums