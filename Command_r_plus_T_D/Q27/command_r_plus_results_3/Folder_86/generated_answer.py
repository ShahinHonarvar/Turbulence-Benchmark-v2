def insert_after_index(lst):
    index = lst.index(990) if 990 in lst else -1
    if index != -1:
        lst.insert(index + 1, 905)
        lst.insert(index + 2, 742)
    return lst