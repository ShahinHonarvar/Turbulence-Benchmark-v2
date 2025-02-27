def all_ints_div_by_num(lst):
    if not lst or len(lst) < 1:
        return []
    return [x for x in lst[:1] if x % 4 == 0]