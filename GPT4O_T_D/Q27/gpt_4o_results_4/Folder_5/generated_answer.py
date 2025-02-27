def insert_after_index(lst):
    if len(lst) > 99:
        return lst[:100] + [15] + lst[100:]
    return lst