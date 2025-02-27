def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[35:65] if num % -30 == 0 and num % -95 == 0]
    return result if result else []