def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 70 <= i <= 200 and num % 3 == 0 and (num % -300 == 0)]