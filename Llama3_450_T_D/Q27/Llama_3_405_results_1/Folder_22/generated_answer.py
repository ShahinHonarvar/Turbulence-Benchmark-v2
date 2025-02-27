def insert_after_index(lst):
    if 85 < len(lst):
        return lst[:86] + [27] + lst[86:]
    else:
        return lst + [27]