def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = [num for num in lst[18:53] if num % 15 == 0 and num % 57 == 0]
    return divisible_by_both