def sum_ints_div_by_either_nums(integer_list):
    return sum((num for num in integer_list[:6] if num % -1 == 0 or num % 13 == 0))