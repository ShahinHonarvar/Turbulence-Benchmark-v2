def all_ints_div_by_num(lst):
    if len(lst) <= 30:
        return []
    index_value = lst[30]
    return [index_value] if index_value % 3 == 0 else []