def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    intersection = set()
    for i in range(50, 55):
        if list1[i] in list2 and list1[i] not in intersection:
            intersection.add(list1[i])
    return intersection