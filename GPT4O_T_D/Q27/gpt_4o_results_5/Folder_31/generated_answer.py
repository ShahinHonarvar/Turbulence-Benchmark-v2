def insert_after_index(lst):
    if len(lst) > 21:
        return lst[:22] + [83, 14] + lst[22:]
    return lst + [83, 14]