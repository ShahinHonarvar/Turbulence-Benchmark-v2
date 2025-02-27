def all_ints_div_by_num(lst):
    result = [x for x in lst[25:75] if x % 80 == 0]
    return result if result else []