def insert_after_index(lst):
    if len(lst) > 48:
        lst = lst[:49] + [86, 77] + lst[49:]
    return lst