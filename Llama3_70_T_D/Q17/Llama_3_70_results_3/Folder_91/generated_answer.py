def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if i <= 4 and i >= 0 and (num % 8 == 0) and (num % -3 == 0)]