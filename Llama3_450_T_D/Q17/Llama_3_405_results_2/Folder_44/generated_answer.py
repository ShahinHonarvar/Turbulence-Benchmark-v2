def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 25 <= i <= 70 and num % 74 == 0 and (num % 15 == 0)]