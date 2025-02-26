def sum_ints_div_by_either_nums(integer_list):
    target_range = integer_list[69:98]
    result = sum((num for num in target_range if num % -90 == 0 or num % -67 == 0))
    return result