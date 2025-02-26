def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[7:10] if num % -9 == 0 or num % -7 == 0))