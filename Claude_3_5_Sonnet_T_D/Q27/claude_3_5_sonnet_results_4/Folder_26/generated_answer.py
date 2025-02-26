def insert_after_index(lst):
    insert_index = lst.index(55) + 1 if 55 in lst else len(lst)
    return lst[:insert_index] + [26, 10] + lst[insert_index:]