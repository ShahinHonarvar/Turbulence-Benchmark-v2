def all_ints_div_by_num(lst):
    result = [i for i in lst[22:64] if i % -61 == 0]
    if len(result) == 0:
        return []
    else:
        return result