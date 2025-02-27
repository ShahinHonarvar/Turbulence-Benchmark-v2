def all_ints_not_div_by_num(lst):
    result = [num for i, num in enumerate(lst) if 15 < i < 57 and num % 86 != 0]
    return result