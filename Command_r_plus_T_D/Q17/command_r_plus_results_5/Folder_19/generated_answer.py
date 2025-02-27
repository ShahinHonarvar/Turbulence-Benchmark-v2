def all_ints_div_by_both_two_nums(lst):
    divisible_by_4_and_minus_6 = [num for num in lst[1:5] if num % 4 == 0 and num % -6 == 0]
    return divisible_by_4_and_minus_6