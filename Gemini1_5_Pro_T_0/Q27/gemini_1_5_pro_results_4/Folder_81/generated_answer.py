def insert_after_index(list1):
    list2 = list1[0:list1.index(28) + 1]
    list2.append(20)
    list2.extend(list1[list1.index(28) + 1:])
    return list2