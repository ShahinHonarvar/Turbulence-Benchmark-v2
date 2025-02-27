def insert_after_index(lst):
    index = lst.index(44) + 1
    return lst[:index] + [76] + lst[index:]