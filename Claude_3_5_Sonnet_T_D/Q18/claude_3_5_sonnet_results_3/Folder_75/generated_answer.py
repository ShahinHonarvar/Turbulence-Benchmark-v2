def sum_ints_div_by_either_nums(integer_list):
    return sum((num for num in integer_list[20:94] if num % -92 == 0 or num % -50 == 0))