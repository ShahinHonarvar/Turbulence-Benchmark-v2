def insert_after_index(lst):
    for i, item in enumerate(lst):
        if item == 85:
            return lst[:i + 1] + [41, 95] + lst[i + 1:]
    return lst