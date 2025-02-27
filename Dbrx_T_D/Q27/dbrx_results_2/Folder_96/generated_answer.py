def insert_after_index(lst):
    index_to_insert = None
    for i in range(len(lst)):
        if lst[i] == 74:
            index_to_insert = i + 1
    if index_to_insert is not None:
        return lst[:index_to_insert] + [51, 29] + lst[index_to_insert:]
    else:
        return lst