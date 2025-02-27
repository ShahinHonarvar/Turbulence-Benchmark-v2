def insert_after_index(list1):
    list2 = list1[:list1.index(96) + 1] + [36] + list1[list1.index(96) + 1:]
    return list2