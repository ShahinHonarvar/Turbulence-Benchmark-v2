def insert_after_index(lst):
    if not lst:
        return lst + [0]
    return lst[:1] + [0] + lst[1:]