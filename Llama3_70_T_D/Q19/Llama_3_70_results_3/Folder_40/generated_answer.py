def all_ints_not_div_by_num(lst):
    try:
        return [i for i in lst[1:-1] if i % 1 != 0]
    except IndexError:
        return []