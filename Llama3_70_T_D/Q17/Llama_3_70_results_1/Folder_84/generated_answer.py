def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 78 <= i <= 81 and num % 76 == 0 and (num % 60 == 0)]