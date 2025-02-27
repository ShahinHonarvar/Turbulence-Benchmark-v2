def insert_after_index(lst):
    if len(lst) > 44:
        return lst[:45] + [40, 27] + lst[45:]
    return lst