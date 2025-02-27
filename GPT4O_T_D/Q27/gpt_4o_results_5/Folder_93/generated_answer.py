def insert_after_index(lst):
    if len(lst) > 36:
        lst = lst[:37] + [54, 13] + lst[37:]
    return lst