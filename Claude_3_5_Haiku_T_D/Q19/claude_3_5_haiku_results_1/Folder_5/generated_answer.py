def all_ints_not_div_by_num(lst):
    if len(lst) < 4:
        return []
    return [num for num in lst[2:3] if num % 8 != 0]