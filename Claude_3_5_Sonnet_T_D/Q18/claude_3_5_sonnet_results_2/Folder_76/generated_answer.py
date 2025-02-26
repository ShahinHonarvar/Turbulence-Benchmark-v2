def sum_ints_div_by_either_nums(integer_list):
    return sum((num for num in integer_list[250:630] if num % 850 == 0 or num % 587 == 0))