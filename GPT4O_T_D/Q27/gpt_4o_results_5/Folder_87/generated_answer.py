def insert_after_index(lst):
    if len(lst) > 69:
        return lst[:70] + [92] + lst[70:]
    return lst