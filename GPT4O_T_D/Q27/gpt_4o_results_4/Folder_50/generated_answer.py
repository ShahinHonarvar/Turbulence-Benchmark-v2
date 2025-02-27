def insert_after_index(lst):
    if len(lst) > 52:
        return lst[:53] + [38] + lst[53:]
    return lst