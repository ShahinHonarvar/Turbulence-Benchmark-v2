def insert_after_index(lst):
    if len(lst) > 8:
        return lst[:9] + [3, 8] + lst[9:]
    return lst + [3, 8]