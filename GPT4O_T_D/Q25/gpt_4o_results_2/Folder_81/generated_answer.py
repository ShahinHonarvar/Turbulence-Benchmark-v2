def insert_at_index(lst):
    return lst[:28] + [20] + lst[28:] if len(lst) >= 28 else lst + [20]