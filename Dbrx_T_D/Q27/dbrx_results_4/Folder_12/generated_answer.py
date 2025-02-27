def insert_after_index(lst):
    index_to_insert = 57
    while index_to_insert >= 0 and index_to_insert < len(lst) - 1:
        if lst[index_to_insert] == 57:
            break
        index_to_insert += 1
    if index_to_insert == len(lst) - 1:
        lst.append(96)
    else:
        lst = lst[:index_to_insert + 1] + [96] + lst[index_to_insert + 1:]
    return lst