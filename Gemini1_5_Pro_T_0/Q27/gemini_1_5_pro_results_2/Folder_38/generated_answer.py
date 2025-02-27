def insert_after_index(list1):
    for i in range(len(list1)):
        if list1[i] == 89:
            list1.insert(i + 1, 86)
            break
    return list1