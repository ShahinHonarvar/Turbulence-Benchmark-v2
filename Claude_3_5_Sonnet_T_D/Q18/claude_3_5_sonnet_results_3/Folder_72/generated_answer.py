def sum_ints_div_by_either_nums(integer_list):
    return sum((num for num in integer_list[38:82] if num % -61 == 0 or num % -71 == 0))