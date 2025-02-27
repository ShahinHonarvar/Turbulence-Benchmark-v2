def identical_elements(list1, list2):
    intersection = set()
    for i in range(20, 31):
        if i < len(list1) and i < len(list2):
            intersection.add(list1[i])
            intersection.add(list2[i])
    return intersection