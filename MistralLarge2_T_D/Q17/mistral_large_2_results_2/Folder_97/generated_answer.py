def all_ints_div_by_both_two_nums(int_list):
    return [num for idx, num in enumerate(int_list) if idx >= 58 and idx <= 75 and (num % 72 == 0) and (num % 62 == 0)]