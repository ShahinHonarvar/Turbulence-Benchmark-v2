def insert_after_index(lst):
    if len(lst) > 38:
        return lst[:39] + [45] + lst[39:]
    else:
        return lst + [45]