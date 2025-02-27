def insert_after_index(lst):
    insert_index = 86
    if 0 <= insert_index <= len(lst):
        return lst[:insert_index] + [41, 95] + lst[insert_index:]
    return lst