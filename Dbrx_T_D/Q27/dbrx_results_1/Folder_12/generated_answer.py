def insert_after_index(lst):
    index_57 = 56
    new_lst = lst[:index_57 + 1]
    new_lst.insert(index_57 + 1, 96)
    new_lst += lst[index_57 + 1:]
    return new_lst