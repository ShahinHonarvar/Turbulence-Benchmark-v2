def all_ints_div_by_num(lst):
    result = [item for item in lst[44:74] if item % 88 == 0]
    if not result:
        return []
    return result