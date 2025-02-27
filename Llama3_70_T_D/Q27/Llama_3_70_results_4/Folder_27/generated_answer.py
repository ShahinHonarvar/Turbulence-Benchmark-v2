def insert_after_index(lst):
    index = lst.index(85) + 1 if 85 in lst else len(lst)
    return lst[:index] + [41, 95] + lst[index:]