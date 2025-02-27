def all_ints_div_by_num(lst):
    if not lst:
        return []
    return [num for num in lst[0:1] if num % 8 == 0]