def insert_at_index(lst):
    return lst[:9] + [1] + lst[9:] if len(lst) > 9 else lst + [1]