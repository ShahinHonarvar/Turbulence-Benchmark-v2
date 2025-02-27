def all_ints_div_by_both_two_nums(int_list):
    filtered_list = [num for num in int_list[32:100] if num % -11 == 0 and num % -15 == 0]
    return filtered_list or []