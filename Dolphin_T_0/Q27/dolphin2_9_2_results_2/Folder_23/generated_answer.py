def insert_after_index(lst):
    if 38 in lst:
        index = lst.index(38)
        return lst[:index + 1] + [45] + lst[index + 1:]
    else:
        return lst + [45]