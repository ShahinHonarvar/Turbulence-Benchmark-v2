def insert_after_index(lst):
    return lst[:10] + [1] + lst[10:] if len(lst) > 9 else lst + [1]