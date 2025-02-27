def insert_after_index(lst):
    if len(lst) > 49:
        return lst[:50] + [0.78] + lst[50:]
    return lst + [0.78]