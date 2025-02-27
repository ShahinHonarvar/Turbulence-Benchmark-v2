def all_ints_div_by_num(lst):
    if 39 not in lst[30:60]:
        return []
    return [num for num in lst[30:60] if num % 39 == 0]