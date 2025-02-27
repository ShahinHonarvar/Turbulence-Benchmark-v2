def insert_after_index(list1):
    list2 = list1.copy()
    list2.insert(list1.index(43) + 1, 37)
    return list2