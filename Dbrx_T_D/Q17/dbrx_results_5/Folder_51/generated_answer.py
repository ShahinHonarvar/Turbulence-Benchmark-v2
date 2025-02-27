def all_ints_div_by_both_two_nums(int_list):
    target_range = int_list[6:10]
    result = [num for num in target_range if num % -1 == 0 and num % -10 == 0]
    return result