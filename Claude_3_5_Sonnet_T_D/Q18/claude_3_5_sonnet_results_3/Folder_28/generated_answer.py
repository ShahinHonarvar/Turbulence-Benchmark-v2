def sum_ints_div_by_either_nums(integer_list):
    return sum((num for num in integer_list[34:82] if num % 27 == 0 or num % 57 == 0))