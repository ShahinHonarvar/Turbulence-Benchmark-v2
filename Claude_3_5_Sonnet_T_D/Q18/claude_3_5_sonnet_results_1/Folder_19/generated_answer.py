def sum_ints_div_by_either_nums(integer_list):
    target_range = integer_list[1:5]
    result = sum((num for num in target_range if num % 4 == 0 or num % -6 == 0))
    return result