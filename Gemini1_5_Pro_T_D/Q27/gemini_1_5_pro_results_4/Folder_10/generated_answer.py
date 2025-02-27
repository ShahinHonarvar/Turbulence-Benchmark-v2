def insert_after_index(list1):
    for i in range(len(list1)):
        if list1[i] == 56:
            list1.insert(i + 1, 54)
            return list1