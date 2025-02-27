def insert_after_index(lst):
    if len(lst) > 7:
        return lst[:8] + [1, 7] + lst[8:]
    return lst