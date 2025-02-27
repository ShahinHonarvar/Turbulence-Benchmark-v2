def insert_after_index(lst):
    idx = 56
    if idx < len(lst):
        return lst[:idx + 1] + [54] + lst[idx + 1:]
    return lst