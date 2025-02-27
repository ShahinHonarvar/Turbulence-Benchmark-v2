def insert_after_index(lst):
    if len(lst) > 32:
        return lst[:33] + [54, 96] + lst[33:]
    return lst