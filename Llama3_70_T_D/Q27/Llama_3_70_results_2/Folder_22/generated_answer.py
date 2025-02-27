def insert_after_index(lst):
    if len(lst) > 85:
        return lst[:86] + [27] + lst[86:]
    else:
        return lst + [27]