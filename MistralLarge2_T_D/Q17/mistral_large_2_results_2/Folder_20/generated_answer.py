def all_ints_div_by_both_two_nums(int_list):
    return [num for i, num in enumerate(int_list) if 48 <= i <= 76 and num % -46 == 0 and (num % -82 == 0)]