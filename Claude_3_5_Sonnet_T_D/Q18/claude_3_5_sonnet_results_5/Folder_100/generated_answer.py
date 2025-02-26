def sum_ints_div_by_either_nums(integer_list):
    return sum((num for num in integer_list[72:94] if num % 32 == 0 or num % 44 == 0))