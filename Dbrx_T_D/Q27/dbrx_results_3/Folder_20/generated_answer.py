def insert_after_index(lst):
    index_to_insert = -1
    for i in range(len(lst)):
        if lst[i] == 32:
            index_to_insert = i + 1
            break
    if index_to_insert != -1:
        lst = lst[:index_to_insert] + [54, 96] + lst[index_to_insert:]
    return lst