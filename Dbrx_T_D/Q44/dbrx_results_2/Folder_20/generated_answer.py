def composite_nums_between_indices(input_list):
    if len(input_list) <= 95 or len(input_list) < 74:
        return set()
    composite_numbers = set()
    for i in range(74, 96):
        num = input_list[i]
        if num > 1 and (not num & 1):
            composite_numbers.add(num)
    return composite_numbers