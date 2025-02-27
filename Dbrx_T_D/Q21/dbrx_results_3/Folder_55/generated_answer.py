def all_ints_div_by_num(lst):
    if len(lst) < 2:
        return []
    return [num for num in lst[:2] if num % 2 == 0]