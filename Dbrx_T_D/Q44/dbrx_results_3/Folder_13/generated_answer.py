def composite_nums_between_indices(input_list):
    if len(input_list) < 98:
        return set()
    composite_set = {num for num in input_list[21:98] if num > 1 and input_list.count(num) > num}
    return composite_set