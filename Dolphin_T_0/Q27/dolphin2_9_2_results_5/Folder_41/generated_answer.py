def insert_after_index(lst):
    index = lst.index(87) + 1
    return lst[:index] + [78, 16] + lst[index:]