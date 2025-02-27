def all_ints_div_by_both_two_nums(lst):
    return [num for i, num in enumerate(lst) if 80 <= i <= 200 and num % 10 == 0 and (num % 1000 == 0)]