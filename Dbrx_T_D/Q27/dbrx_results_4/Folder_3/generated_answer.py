def insert_after_index(lst):
    index_31 = None
    for i in range(len(lst)):
        if lst[i] == 31:
            index_31 = i
    if index_31 is not None:
        return lst[:index_31 + 1] + [88, 51] + lst[index_31 + 1:]
    else:
        return lst