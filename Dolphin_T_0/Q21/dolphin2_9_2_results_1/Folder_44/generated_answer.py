def all_ints_div_by_num(lst):
    range_lst = lst[66:82]
    result = [i for i in range_lst if i % 77 == 0]
    if not result:
        return []
    return result