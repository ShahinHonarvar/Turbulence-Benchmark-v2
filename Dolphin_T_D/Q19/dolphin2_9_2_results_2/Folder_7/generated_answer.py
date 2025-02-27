def all_ints_not_div_by_num(lst):
    result = [i for i in lst[495:826] if i % -201 != 0]
    if not result:
        return []
    return result