def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 31 <= i <= 50 and num % 81 == 0 and (num % 64 == 0)]