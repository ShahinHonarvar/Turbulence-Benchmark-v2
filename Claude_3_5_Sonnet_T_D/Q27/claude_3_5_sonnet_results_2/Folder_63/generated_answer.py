def insert_after_index(lst):
    insert_index = 77 if len(lst) > 77 else len(lst)
    return lst[:insert_index] + [15, 51] + lst[insert_index:]