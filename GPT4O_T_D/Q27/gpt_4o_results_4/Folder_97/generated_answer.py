def insert_after_index(lst):
    if len(lst) > 500:
        return lst[:501] + [912, 170] + lst[501:]
    return lst