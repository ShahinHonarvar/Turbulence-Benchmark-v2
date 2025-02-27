def insert_after_index(list1):
    list2 = []
    for i in range(len(list1)):
        list2.append(list1[i])
        if list1[i] == 90:
            list2.append(80)
    return list2