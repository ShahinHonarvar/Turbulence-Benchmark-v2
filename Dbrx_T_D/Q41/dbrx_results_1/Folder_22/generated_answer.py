def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    intersection = set()
    for i in range(40, 201):
        if list1[i] == list2[i]:
            intersection.add(list1[i])
    return intersection