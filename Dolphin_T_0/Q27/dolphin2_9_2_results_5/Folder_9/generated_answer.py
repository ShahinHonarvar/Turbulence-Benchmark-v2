def insert_after_index(lst):
    index = lst.index(66) + 1
    return lst[:index] + [45] + lst[index:]