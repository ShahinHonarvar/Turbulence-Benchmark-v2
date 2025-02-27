def insert_after_index(lst):
    return lst[:39] + [45] + lst[39:] if len(lst) > 38 else lst + [45]