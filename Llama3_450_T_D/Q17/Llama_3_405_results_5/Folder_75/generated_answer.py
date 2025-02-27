def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 20 <= i <= 93 and num % -92 == 0 and (num % -50 == 0)]