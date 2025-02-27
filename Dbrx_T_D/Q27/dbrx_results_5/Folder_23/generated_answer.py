def insert_after_index(lst):
    index_to_insert = 38
    while index_to_insert >= 0 and index_to_insert < len(lst) - 1 and (lst[index_to_insert + 1] != 45):
        index_to_insert += 1
    if index_to_insert == len(lst) - 1:
        lst.append(45)
    else:
        lst = lst[:index_to_insert + 1] + [45] + lst[index_to_insert + 1:]
    return lst