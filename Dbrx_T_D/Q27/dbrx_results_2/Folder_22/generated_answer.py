def insert_after_index(lst):
    for i, item in enumerate(lst):
        if item == 85:
            return lst[:i + 1] + [27] + lst[i + 1:]
    return lst + [27]