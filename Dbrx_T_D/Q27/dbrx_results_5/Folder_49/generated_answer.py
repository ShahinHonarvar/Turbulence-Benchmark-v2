def insert_after_index(lst):
    index_to_insert = 38
    for i in range(len(lst)):
        if i == index_to_insert:
            return lst[:i + 1] + [27, 34] + lst[i + 1:]
    return lst + [27, 34]