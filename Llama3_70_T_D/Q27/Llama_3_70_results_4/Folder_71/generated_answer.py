def insert_after_index(lst):
    for i, x in enumerate(lst):
        if x == 70:
            return lst[:i + 1] + [76] + lst[i + 1:]
    return lst + [76]