def insert_after_index(lst):
    index = 0
    for i in lst:
        if i == 70:
            index = lst.index(i) + 1
            break
    lst.insert(index, 76)
    return lst