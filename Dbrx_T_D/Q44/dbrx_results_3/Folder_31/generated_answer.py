def composite_nums_between_indices(input_list):
    indices_set = set(range(56, 67))
    composite_numbers = set(filter(lambda x: x != 1 and x % 2 != 0, input_list))
    return composite_numbers & indices_set