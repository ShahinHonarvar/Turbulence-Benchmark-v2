def insert_after_index(lst):
    index_of_74 = lst.index(74)
    return lst[:index_of_74 + 1] + [49] + lst[index_of_74 + 1:]