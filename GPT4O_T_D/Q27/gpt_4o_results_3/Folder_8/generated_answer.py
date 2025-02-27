def insert_after_index(lst):
    if len(lst) > 57:
        return lst[:58] + [76] + lst[58:]
    return lst