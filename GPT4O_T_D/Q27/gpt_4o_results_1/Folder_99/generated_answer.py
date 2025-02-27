def insert_after_index(lst):
    if 295 < len(lst):
        return lst[:296] + [276, 376] + lst[296:]
    return lst