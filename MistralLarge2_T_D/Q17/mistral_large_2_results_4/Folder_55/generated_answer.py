def all_ints_div_by_both_two_nums(int_list):
    return [num for i, num in enumerate(int_list) if 0 <= i <= 9 and num % 10 == 0 and (num % 100 == 0)]