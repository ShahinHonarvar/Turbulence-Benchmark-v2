def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    intersect = set()
    for i in range(max(22, len(list1) - 50), min(len(list2), 50 + 1)):
        if list1[i] == list2[i]:
            intersect.add(list1[i])
    return intersect