def sum_ints_div_by_either_nums(integer_list):
    target_range = integer_list[55:85]
    result = sum((num for num in target_range if num % -24 == 0 or num % -11 == 0))
    return result