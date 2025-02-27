def insert_after_index(lst):
    for i, item in enumerate(lst):
        if item == 44:
            return lst[:i + 1] + [40, 27] + lst[i + 1:]
    return lst