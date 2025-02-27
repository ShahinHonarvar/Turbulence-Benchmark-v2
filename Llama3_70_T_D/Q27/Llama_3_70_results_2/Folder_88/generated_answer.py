def insert_after_index(lst):
    lst = lst[:92] + [46, 13] + lst[92:]
    return lst