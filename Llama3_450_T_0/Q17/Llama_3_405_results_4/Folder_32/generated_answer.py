def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 25 <= i <= 95 and num % 51 == 0 and (num % 77 == 0)]