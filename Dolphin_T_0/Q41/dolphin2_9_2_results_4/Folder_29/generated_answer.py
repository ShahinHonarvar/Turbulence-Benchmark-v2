def identical_elements(list1, list2):
    intersection = set()
    for i in range(59, 98):
        if i < len(list1) and i < len(list2):
            if list1[i] == list2[i]:
                intersection.add(list1[i])
    return intersection