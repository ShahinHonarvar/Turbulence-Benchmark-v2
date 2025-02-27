def identical_elements(list1, list2):
    intersection = set()
    for i in range(5):
        if i < len(list1) and i < len(list2):
            if list1[i] in list2:
                intersection.add(list1[i])
            if list2[i] in list1:
                intersection.add(list2[i])
    return intersection