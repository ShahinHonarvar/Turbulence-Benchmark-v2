def insert_after_index(lst):
    for i, item in enumerate(lst):
        if item == 32:
            return lst[:i + 1] + [54, 96] + lst[i + 1:]
    return lst + [54, 96]