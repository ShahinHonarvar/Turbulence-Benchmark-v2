def all_ints_div_by_num(lst):
    if not lst or len(lst) < 50 or len(lst) < 54:
        return []
    return [num for num in lst[50:55] if num % 84 == 0]