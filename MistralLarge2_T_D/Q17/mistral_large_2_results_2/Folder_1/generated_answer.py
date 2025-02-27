def all_ints_div_by_both_two_nums(int_list):
    return [num for i, num in enumerate(int_list) if 10 <= i <= 28 and num % -61 == 0 and (num % -64 == 0)]