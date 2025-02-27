def insert_after_index(lst):
    index_to_insert = 28
    for i in range(len(lst)):
        if i == index_to_insert:
            lst = lst[:i + 1] + [20] + lst[i + 1:]
    return lst