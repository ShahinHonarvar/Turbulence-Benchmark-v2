def all_ints_div_by_both_two_nums(num_list):
    return [num for num in num_list[0:6] if num % -1 == 0 and num % 13 == 0]