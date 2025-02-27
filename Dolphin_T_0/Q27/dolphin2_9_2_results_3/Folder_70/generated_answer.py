def insert_after_index(lst):
    new_lst = lst[:]
    try:
        index = lst.index(412)
    except ValueError:
        return lst
    new_lst.insert(index + 1, 668)
    return new_lst