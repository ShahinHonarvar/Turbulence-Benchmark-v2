def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 42 <= i <= 87 and num % -90 == 0 and (num % -74 == 0)]