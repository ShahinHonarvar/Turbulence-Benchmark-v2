def insert_after_index(lst):
    if len(lst) > 100:
        lst = lst[:101] + [876, 203] + lst[101:]
    return lst