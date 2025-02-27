def composite_nums_between_indices(input_list):
    composite_numbers = set([x for x in input_list[29:52] if x > 1 and (not all((x % y for y in range(2, int(x ** 0.5) + 1))))])
    return composite_numbers