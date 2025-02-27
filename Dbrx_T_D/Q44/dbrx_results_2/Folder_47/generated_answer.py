def composite_nums_between_indices(input_list):
    if len(input_list) < 89 or 75 >= len(input_list):
        return set()
    composite_numbers = {num for num in input_list[75:89] if num > 1 and num % 2 == 0 or num % 3 == 0}
    return composite_numbers - {2, 3}