def insert_after_index(lst):
    for i, item in enumerate(lst):
        if item == 97:
            return lst[:i + 1] + [47, 22] + lst[i + 1:]
    return lst