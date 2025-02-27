def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 66:
            return lst[:i + 1] + [45] + lst[i + 1:]
    return lst