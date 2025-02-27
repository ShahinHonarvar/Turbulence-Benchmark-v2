def insert_after_index(lst):
    if len(lst) > 93:
        return lst[:94] + [33, 78] + lst[94:]
    return lst