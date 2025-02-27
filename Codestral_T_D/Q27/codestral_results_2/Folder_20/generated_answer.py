def insert_after_index(lst):
    if 32 < len(lst):
        return lst[:33] + [54, 96] + lst[33:]
    else:
        return lst