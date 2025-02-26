def sum_ints_div_by_either_nums(integer_list):
    target_range = integer_list[51:77]
    result = sum((num for num in target_range if num % -90 == 0 or num % -59 == 0))
    return result