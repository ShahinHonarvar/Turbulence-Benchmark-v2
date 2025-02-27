def insert_after_index(lst):
    if len(lst) > 62:
        return lst[:63] + [51] + lst[63:]
    return lst