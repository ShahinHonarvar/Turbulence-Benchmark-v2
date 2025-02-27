def all_ints_div_by_num(lst):
    if len(lst) < 5:
        return []
    return [num for num in lst[4:6] if num % 3 == 0]