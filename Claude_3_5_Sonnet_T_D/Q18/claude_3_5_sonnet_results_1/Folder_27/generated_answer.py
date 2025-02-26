def sum_ints_div_by_either_nums(integer_list):
    target_range = integer_list[20:36]
    result = sum((num for num in target_range if num % -36 == 0 or num % -89 == 0))
    return result