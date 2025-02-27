def all_ints_div_by_num(lst):
    result = [i for i in lst[26:75] if i % 80 == 0]
    return result if result else []