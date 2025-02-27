def all_ints_div_by_both_two_nums(num_list):
    return [num for num in num_list if num % 1 == 0 and num % -1 == 0 and (num % 2 == 0)]