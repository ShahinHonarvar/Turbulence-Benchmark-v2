def insert_after_index(lst):
    index = lst.index(93) + 1 if 93 in lst else len(lst)
    return lst[:index] + [33, 78] + lst[index:]