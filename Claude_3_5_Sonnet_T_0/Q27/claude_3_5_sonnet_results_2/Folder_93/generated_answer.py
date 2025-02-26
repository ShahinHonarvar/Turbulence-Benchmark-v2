def insert_after_index(lst):
    new_list = lst.copy()
    insert_index = 37 if len(lst) > 37 else len(lst)
    new_list[insert_index:insert_index] = [54, 13]
    return new_list