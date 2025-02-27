def all_ints_div_by_both_two_nums(int_list):
    return [num for i, num in enumerate(int_list) if 80 <= i <= 200 and num % 10 == 0 and (num % 1000 == 0)]