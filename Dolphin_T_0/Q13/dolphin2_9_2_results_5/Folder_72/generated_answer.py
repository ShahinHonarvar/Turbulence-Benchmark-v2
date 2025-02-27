def find_second_largest_num(lst):
    restricted_lst = lst[29:52]
    if len(restricted_lst) < 2:
        return None
    else:
        return sorted(restricted_lst)[-2]