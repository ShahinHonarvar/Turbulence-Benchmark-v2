def all_even_ints_inclusive(lst):
    if len(lst) < 2:
        return []
    sub_lst = lst[0:2]
    return [x for x in sub_lst if x % 2 == 0]