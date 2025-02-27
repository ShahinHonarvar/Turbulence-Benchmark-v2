def insert_after_index(lst):
    try:
        idx = lst.index(66)
        return lst[:idx + 1] + [45] + lst[idx + 1:]
    except ValueError:
        return lst + [45]