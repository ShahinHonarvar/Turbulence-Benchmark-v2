def all_ints_div_by_both_two_nums(lst):
    divisible_by_45_and_20 = [num for num in lst[13:19] if num % 45 == 0 and num % 20 == 0]
    return divisible_by_45_and_20