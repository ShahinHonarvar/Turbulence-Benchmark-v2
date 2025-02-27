def all_ints_div_by_both_two_nums(lst):
    valid_nums = [num for num in lst[44:60] if num % 39 == 0 and num % 15 == 0]
    return valid_nums