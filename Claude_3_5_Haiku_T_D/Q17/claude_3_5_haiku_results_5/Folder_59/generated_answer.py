def all_ints_div_by_both_two_nums(input_list):
    return [num for num in input_list[:9] if num % -3 == 0 and num % 8 == 0]