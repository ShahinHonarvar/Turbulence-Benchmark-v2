def insert_after_index(lst):
    if len(lst) > 41:
        lst = lst[:42] + [74, 70] + lst[42:]
    return lst