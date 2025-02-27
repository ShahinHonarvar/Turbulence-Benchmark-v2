def all_ints_div_by_both_two_nums(int_list):
    return [num for i, num in enumerate(int_list[25:81]) if num % -20 == 0 and num % -26 == 0]