def insert_after_index(lst):
    if len(lst) > 20:
        return lst[:21] + [80] + lst[21:]
    return lst