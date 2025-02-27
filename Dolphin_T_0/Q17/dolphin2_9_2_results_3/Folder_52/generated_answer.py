def all_ints_div_by_both_two_nums(lst):
    result = [num for num in lst[48:60] if num % 58 == 0 and num % 88 == 0]
    return result if result else []