def all_ints_div_by_num(lst):
    if len(lst) < 11:
        return []
    return [num for num in lst[10:11] if num % 1 == 0]