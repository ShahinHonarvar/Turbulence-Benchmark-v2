def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[10:29] if num % -61 == 0 or num % -64 == 0))