def insert_after_index(lst):
    new_list = lst.copy()
    insert_index = 599 if 598 < len(lst) else len(lst)
    new_list[insert_index:insert_index] = [385, 999]
    return new_list