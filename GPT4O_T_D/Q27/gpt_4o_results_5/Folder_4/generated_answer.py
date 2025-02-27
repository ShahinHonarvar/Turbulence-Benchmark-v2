def insert_after_index(lst):
    if len(lst) > 60:
        lst = lst[:61] + [80, 74] + lst[61:]
    return lst