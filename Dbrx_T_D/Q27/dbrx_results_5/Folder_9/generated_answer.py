def insert_after_index(lst):
    index_to_insert = next((i for i in range(len(lst)) if lst[i] == 66), None)
    if index_to_insert is not None:
        return lst[:index_to_insert + 1] + [45] + lst[index_to_insert + 1:]
    else:
        return lst