def insert_after_index(lst):
    if len(lst) > 44:
        return lst[:45] + [76] + lst[45:]
    return lst