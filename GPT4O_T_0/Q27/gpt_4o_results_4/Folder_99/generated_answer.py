def insert_after_index(lst):
    if len(lst) > 295:
        return lst[:296] + [276, 376] + lst[296:]
    return lst