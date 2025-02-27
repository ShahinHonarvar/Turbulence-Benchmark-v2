def all_ints_not_div_by_num(lst):
    range_start, range_end = (38, 81)
    result = [x for x in lst[range_start:range_end] if x % 49 != 0]
    return result