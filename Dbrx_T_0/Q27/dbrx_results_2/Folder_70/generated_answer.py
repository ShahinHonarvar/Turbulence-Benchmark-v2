def insert_after_index(lst):
    index_412 = lst.index(412)
    return lst[:index_412 + 1] + [668] + lst[index_412 + 1:]