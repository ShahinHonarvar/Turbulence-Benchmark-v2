def insert_after_index(lst):
    if 60 in lst:
        index = lst.index(60) + 1
        lst[index:index] = [80, 74]
    return lst