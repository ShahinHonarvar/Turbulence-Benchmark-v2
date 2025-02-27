def insert_after_index(lst):
    if len(lst) > 85:
        lst = lst[:86] + [41, 95] + lst[86:]
    return lst