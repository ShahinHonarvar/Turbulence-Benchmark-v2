def insert_at_index(lst):
    if len(lst) < 99:
        return lst + [15]
    return lst[:99] + [15] + lst[99:]