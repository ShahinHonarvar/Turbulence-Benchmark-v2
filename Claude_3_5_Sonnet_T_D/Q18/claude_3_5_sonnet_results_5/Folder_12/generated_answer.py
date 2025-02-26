def sum_ints_div_by_either_nums(integer_list):
    target_range = integer_list[35:65]
    result = sum((num for num in target_range if num % -30 == 0 or num % -95 == 0))
    return result