def insert_after_index(lst):
    if 44 < len(lst):
        return lst[:45] + [40, 27] + lst[45:]
    else:
        return lst + [40, 27]