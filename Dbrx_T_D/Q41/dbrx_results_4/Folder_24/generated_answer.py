def identical_elements(list1, list2):
    intersection = set()
    for i in range(74, 96):
        if list1[i] in list2 and list1[i] not in intersection:
            intersection.add(list1[i])
        elif list2[i] in list1 and list2[i] not in intersection:
            intersection.add(list2[i])
    return intersection