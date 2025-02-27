def insert_after_index(lst):
    if len(lst) > 35:
        return lst[:36] + [90, 76] + lst[36:]
    return lst