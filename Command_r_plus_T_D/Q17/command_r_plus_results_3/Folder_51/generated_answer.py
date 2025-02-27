def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = [num for num in lst[6:10] if num % -1 == 0 and num % -10 == 0]
    return divisible_by_both