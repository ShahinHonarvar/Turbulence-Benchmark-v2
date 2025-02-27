def insert_after_index(lst):
    lst = lst[:64] + [99] + lst[64:]
    return lst