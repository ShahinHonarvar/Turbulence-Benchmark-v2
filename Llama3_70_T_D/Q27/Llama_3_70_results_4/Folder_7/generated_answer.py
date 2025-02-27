def insert_after_index(lst):
    if 323 in lst:
        index = lst.index(323) + 1
        return lst[:index] + [389, 303] + lst[index:]
    else:
        return lst