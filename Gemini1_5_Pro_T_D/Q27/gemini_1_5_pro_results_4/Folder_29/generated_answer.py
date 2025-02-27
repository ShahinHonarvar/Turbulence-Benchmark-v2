def insert_after_index(list1):
    list2 = list1.copy()
    for i in range(len(list2)):
        if list2[i] == 96:
            list2.insert(i + 1, 36)
            break
    return list2