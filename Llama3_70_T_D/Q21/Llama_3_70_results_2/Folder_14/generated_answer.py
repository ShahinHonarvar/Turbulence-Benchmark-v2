def all_ints_div_by_num(lst):
    try:
        return [i for i in lst[7:9] if i % 8 == 0]
    except IndexError:
        return []