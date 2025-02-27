def insert_after_index(lst):
    if len(lst) > 55:
        return lst[:56] + [26, 10] + lst[56:]
    return lst