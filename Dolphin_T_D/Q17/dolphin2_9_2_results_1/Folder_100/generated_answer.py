def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[72:94] if num % 32 == 0 and num % 44 == 0]
    return result