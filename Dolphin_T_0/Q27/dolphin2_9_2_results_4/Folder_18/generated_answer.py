def insert_after_index(lst):
    position = lst.index(696) if 696 in lst else len(lst)
    lst.insert(position + 1, 477)
    return lst