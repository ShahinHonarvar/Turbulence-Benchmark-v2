def all_ints_div_by_both_two_nums(int_list):
    result_list = [num for num in int_list[35:65] if num % -30 == 0 and num % -95 == 0]
    return result_list