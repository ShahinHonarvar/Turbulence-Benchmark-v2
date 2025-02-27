def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 10 <= i <= 28 and num % -61 == 0 and (num % -64 == 0)]