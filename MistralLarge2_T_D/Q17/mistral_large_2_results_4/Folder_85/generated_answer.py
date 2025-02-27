def all_ints_div_by_both_two_nums(int_list):
    return [num for num in int_list[1:9] if num % -9 == 0 and num % -3 == 0]