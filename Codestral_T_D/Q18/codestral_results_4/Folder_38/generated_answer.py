def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[10:77] if num % -40 == 0 or num % -12 == 0))