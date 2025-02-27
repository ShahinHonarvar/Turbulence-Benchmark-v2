def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 38 <= i <= 81 and num % -61 == 0 and (num % -71 == 0)]