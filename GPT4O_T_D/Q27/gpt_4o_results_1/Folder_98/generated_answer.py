def insert_after_index(lst):
    if len(lst) > 9:
        return lst[:10] + [1] + lst[10:]
    return lst + [1]