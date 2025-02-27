def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst[:6]) if num % -1 == 0 and num % 13 == 0]