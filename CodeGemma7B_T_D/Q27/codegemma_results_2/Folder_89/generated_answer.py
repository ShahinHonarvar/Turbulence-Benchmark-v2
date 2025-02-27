def insert_after_index(lst):
    insert_index = 63
    new_lst = lst[:insert_index + 1] + [51] + lst[insert_index + 1:]
    return new_lst