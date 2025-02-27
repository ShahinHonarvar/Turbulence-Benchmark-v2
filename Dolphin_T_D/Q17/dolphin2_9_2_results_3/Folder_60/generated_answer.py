def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[10:80] if num % -74 == 0 and num % -58 == 0]
    return result