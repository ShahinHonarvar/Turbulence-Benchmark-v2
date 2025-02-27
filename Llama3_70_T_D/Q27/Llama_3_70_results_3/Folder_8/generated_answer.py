def insert_after_index(lst):
    if 57 in lst:
        insert_index = lst.index(57) + 1
        return lst[:insert_index] + [76] + lst[insert_index:]
    else:
        return lst