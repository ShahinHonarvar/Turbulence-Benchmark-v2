def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[50:93] if num % -94 == 0 or num % -95 == 0))