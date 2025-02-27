def insert_after_index(lst):
    index_412 = lst.index(412)
    element_after_412 = lst[index_412 + 1]
    lst.insert(index_412 + 1, 668)
    return lst