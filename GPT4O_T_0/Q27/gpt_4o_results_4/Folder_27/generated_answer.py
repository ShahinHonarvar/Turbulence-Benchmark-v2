def insert_after_index(lst):
    if 85 < len(lst):
        return lst[:86] + [41, 95] + lst[86:]
    return lst