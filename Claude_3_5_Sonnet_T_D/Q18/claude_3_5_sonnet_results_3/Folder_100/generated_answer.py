def sum_ints_div_by_either_nums(int_list):
    valid_range = int_list[72:94]
    result = sum((num for num in valid_range if num % 32 == 0 or num % 44 == 0))
    return result