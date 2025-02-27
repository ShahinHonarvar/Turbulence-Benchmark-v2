def identical_elements(list1, list2):
    intersection = set()
    if len(list1) != len(list2):
        return intersection
    for i in range(75, 86):
        if list1[i] in list2[i] and list1[i] not in intersection:
            intersection.add(list1[i])
    return intersection