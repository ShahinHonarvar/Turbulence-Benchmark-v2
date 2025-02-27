def insert_after_index(lst):
    if 93 < len(lst):
        return lst[:94] + [33, 78] + lst[94:]
    else:
        return lst + [None] * (93 - len(lst)) + [33, 78]