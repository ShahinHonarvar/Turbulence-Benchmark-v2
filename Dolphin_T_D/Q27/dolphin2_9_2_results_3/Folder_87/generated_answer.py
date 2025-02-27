def insert_after_index(lst):
    index = lst.index(69) + 1
    return lst[:index] + [92] + lst[index:]