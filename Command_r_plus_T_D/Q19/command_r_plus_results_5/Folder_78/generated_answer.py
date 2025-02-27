def all_ints_not_div_by_num(lst):
    result = [num for i, num in enumerate(lst[10:55]) if num % 36 != 0]
    return result