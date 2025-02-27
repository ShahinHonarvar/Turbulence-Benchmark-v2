def all_ints_div_by_both_two_nums(int_list):
    return [num for num in int_list if num % 1 == 0 and num % 2 == 0 and (num >= int_list[0]) and (num <= int_list[1])]