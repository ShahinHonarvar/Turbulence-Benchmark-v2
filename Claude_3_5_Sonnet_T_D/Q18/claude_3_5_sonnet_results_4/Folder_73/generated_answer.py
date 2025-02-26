def sum_ints_div_by_either_nums(integer_list):
    return sum((num for num in integer_list[81:87] if num % -33 == 0 or num % -62 == 0))