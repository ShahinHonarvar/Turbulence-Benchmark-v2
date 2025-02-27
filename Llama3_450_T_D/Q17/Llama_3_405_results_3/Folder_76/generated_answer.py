def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 250 <= i <= 629 and num % 850 == 0 and (num % 587 == 0)]