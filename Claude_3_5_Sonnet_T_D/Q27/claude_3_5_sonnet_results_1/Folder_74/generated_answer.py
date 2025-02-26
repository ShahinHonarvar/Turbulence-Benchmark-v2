def insert_after_index(lst):
    new_list = lst.copy()
    insert_index = 42 if len(lst) > 42 else len(lst)
    new_list[insert_index:insert_index] = [74, 70]
    return new_list