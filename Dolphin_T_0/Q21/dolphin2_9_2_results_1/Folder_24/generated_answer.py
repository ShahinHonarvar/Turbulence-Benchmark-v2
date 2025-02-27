def all_ints_div_by_num(lst):
    result = [i for i in lst[12:78] if i % -19 == 0]
    if not result:
        return []
    return result