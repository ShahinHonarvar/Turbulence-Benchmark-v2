def insert_after_index(lst):
    index_of_35 = lst.index(35)
    return lst[:index_of_35 + 1] + [88] + lst[index_of_35 + 1:]