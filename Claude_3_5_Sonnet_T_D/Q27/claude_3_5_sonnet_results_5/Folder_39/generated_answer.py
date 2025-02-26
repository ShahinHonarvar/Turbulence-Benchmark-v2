def insert_after_index(lst):
    insert_index = 98
    if insert_index <= len(lst):
        return lst[:insert_index] + [47, 22] + lst[insert_index:]
    else:
        return lst + [47, 22]