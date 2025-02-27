def all_ints_div_by_both_two_nums(int_list):
    return [num for i, num in enumerate(int_list) if 38 <= i <= 52 and num % -41 == 0 and (num % -47 == 0)]