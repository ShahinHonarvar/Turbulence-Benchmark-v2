def all_ints_div_by_both_two_nums(lst):
    divisible_nums = [num for num in lst[58:82] if num % 55 == 0 and num % 10 == 0]
    return divisible_nums