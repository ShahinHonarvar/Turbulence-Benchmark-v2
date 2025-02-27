def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 85:
            index_to_insert = i + 1
            lst = lst[:index_to_insert] + [27] + lst[index_to_insert:]
    return lst