def all_ints_div_by_both_two_nums(int_list):
    target_range = int_list[48:77]
    result = [num for num in target_range if num % -46 == 0 and num % -82 == 0]
    return result