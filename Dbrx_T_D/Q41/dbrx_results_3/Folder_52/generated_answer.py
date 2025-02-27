def identical_elements(list1, list2):
    intersection = set()
    for i in range(28, 39):
        if list1[i] in list2[i] and list1[i] not in intersection:
            intersection.add(list1[i])
    return intersection