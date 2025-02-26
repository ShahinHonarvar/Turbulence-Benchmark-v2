def sum_ints_div_by_either_nums(int_list):
    target_range = int_list[86:90]
    result = sum((num for num in target_range if num % -61 == 0 or num % -79 == 0))
    return result