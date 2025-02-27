def insert_after_index(lst):
    return lst[:30] + [28, 53] + lst[30:] if len(lst) > 30 else lst + [28, 53]