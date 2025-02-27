def all_ints_not_div_by_num(lst):
    result = [num for i, num in enumerate(lst) if num % -6 != 0 and 0 < i < 6]
    return result