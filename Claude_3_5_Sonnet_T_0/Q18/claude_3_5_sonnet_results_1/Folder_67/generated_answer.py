def sum_ints_div_by_either_nums(integer_list):
    target_range = integer_list[24:33]
    result = sum((num for num in target_range if num % 35 == 0 or num % 87 == 0))
    return result