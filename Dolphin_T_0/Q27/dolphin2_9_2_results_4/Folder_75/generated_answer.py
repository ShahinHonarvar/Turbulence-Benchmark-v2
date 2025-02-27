def insert_after_index(lst):
    for i, v in enumerate(lst):
        if v == 99:
            return lst[:i + 1] + [99] + lst[i + 1:]
    return lst + [99]