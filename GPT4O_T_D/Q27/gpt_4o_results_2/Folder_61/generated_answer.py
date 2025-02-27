def insert_after_index(lst):
    if len(lst) > 4:
        return lst[:5] + [7] + lst[5:]
    return lst + [7]