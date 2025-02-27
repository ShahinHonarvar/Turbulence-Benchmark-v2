def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = [num for num in lst[1:9] if num % -9 == 0 and num % -3 == 0]
    return divisible_by_both