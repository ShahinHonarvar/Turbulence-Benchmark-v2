def insert_after_index(lst):
    if len(lst) > 91:
        return lst[:92] + [46, 13] + lst[92:]
    return lst