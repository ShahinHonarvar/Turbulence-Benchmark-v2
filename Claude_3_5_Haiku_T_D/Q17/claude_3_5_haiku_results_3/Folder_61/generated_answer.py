def all_ints_div_by_both_two_nums(lst):
    divisible_ints = [num for num in lst[0:7] if num % -5 == 0 and num % -6 == 0]
    return divisible_ints