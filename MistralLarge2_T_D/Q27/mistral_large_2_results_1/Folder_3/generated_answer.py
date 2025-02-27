def insert_after_index(lst):
    lst = lst[:32] + [88, 51] + lst[32:]
    return lst