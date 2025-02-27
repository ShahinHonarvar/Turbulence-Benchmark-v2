def insert_after_index(lst):
    try:
        index = lst.index(66)
        return lst[:index + 1] + [45] + lst[index + 1:]
    except ValueError:
        return 'Index 66 not found in list.'