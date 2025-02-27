def insert_after_index(lst):
    if len(lst) > 51:
        return lst[:52] + [304.62] + lst[52:]
    return lst