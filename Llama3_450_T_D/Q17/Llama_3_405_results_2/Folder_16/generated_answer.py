def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 55 <= i <= 80 and num % 22 == 0 and (num % 32 == 0)]