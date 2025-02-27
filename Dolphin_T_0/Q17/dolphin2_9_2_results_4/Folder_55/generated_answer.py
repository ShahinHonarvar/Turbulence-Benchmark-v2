def all_ints_div_by_both_two_nums(int_lst):
    return [num for num in int_lst[:10] if num % 10 == 0 and num % 100 == 0]