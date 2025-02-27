def insert_after_index(lst):
    if 44 in [i for i in range(len(lst))]:
        new_list = lst[:45] + [76] + lst[45:]
    else:
        new_list = lst + [76]
    return new_list