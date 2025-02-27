def all_ints_div_by_both_two_nums(num_list):
    valid_nums = num_list[25:96]
    return [num for num in valid_nums if num % 51 == 0 and num % 77 == 0]