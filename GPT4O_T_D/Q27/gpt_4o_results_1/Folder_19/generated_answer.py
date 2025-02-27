def insert_after_index(lst):
    return lst[:50] + [0.78] + lst[50:] if len(lst) > 49 else lst + [0.78]