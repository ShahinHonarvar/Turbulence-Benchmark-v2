def all_ints_div_by_both_two_nums(int_list):
    return [num for i, num in enumerate(int_list) if 77 <= i <= 87 and num % 23 == 0 and (num % 57 == 0)]