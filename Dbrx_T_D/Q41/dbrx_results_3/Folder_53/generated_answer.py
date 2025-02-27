def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    intersection = set()
    for i in range(200, len(list1) - 200 + 1):
        if list1[i] == list2[i] and list1[i] not in intersection:
            intersection.add(list1[i])
    return intersection