def insert_after_index(lst):
    if 93 < len(lst) - 1:
        return lst[:94] + [33, 78] + lst[94:]
    else:
        return lst + [33, 78]