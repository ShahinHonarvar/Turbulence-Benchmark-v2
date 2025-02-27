def insert_after_index(lst):
    return lst[:43] + [53] + lst[43:] if len(lst) > 42 else lst + [53]