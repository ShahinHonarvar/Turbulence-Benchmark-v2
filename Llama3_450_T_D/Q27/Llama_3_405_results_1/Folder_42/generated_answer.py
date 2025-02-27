def insert_after_index(lst):
    if 44 in lst:
        index = lst.index(44) + 1
        return lst[:index] + [40, 27] + lst[index:]
    else:
        return lst