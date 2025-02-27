def all_ints_div_by_num(lst):
    result = [i for i in lst[1:9] if i % 6 == 0]
    return result or []