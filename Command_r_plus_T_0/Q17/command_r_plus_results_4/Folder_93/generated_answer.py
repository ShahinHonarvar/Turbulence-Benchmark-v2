def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = [num for num in lst[86:90] if num % -61 == 0 and num % -79 == 0]
    return divisible_by_both