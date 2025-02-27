def composite_nums_between_indices(num_list):
    indices_range = num_list[314:348]
    composite_numbers = set(filter(lambda x: x > 1 and x % 2 != 0 and (x % 3 != 0), indices_range))
    return composite_numbers