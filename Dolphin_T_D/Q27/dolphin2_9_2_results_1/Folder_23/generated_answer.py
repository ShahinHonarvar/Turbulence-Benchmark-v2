def insert_after_index(lst):
    index_38 = lst.index(38)
    return lst[:index_38 + 1] + [45] + lst[index_38 + 1:]