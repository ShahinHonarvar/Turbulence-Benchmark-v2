def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst, start=0) if 48 <= i <= 59 and num % 88 == 0 and (num % 58 == 0)]