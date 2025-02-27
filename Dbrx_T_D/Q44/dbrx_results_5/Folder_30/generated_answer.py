def composite_nums_between_indices(integer_list):
    composite_numbers = {i for i in integer_list[19:93] if i > 1 and any((i % j == 0 for j in range(2, i)))}
    return composite_numbers