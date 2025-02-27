def insert_after_index(lst):
    try:
        i = lst.index(66)
        return lst[:i + 1] + [45] + lst[i + 1:]
    except ValueError:
        return lst