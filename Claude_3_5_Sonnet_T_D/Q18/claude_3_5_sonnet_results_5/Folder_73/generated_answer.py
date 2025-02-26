def sum_ints_div_by_either_nums(integer_list):
    target_range = integer_list[81:87]
    return sum((num for num in target_range if num % -33 == 0 or num % -62 == 0))