def insert_after_index(lst):
    index = 93
    to_insert = [33, 78]
    lst = lst[:index + 1] + to_insert + lst[index + 1:]
    return lst