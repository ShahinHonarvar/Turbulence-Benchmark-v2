def insert_after_index(lst):
    for i, x in enumerate(lst):
        if x == 44:
            return lst[:i + 1] + [40, 27] + lst[i + 1:]
    return lst + [40, 27]