def insert_after_index(lst):
    for i, item in enumerate(lst):
        if item == 36:
            return lst[:i + 1] + [54, 13] + lst[i + 1:]
    return lst