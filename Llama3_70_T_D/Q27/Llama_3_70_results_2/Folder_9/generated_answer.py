def insert_after_index(lst):
    if len(lst) > 66:
        return lst[:67] + [45] + lst[67:]
    else:
        return lst