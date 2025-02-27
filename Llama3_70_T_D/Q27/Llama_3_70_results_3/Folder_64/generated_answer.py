def insert_after_index(lst):
    if len(lst) > 8:
        return lst[:8] + [3, 8] + lst[8:]
    else:
        return lst + [3, 8]