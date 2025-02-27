def insert_at_index(lst):
    lst_copy = lst.copy()
    lst_copy[100:100] = [876, 203]
    return lst_copy