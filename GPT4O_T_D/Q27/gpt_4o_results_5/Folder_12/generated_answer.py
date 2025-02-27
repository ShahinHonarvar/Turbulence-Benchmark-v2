def insert_after_index(lst):
    if len(lst) > 57:
        return lst[:58] + [96] + lst[58:]
    return lst