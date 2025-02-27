def composite_nums_between_indices(num_list):
    composite_nums = {i for i in num_list[12:93] if i > 1 and (not i & 1) and (i != i | 1) or i in {4, 6, 8, 9, 10} or i % 6 in {1, 5}}
    return composite_nums