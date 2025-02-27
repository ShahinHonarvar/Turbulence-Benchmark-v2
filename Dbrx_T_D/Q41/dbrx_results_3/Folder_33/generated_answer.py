def identical_elements(list1, list2):
    intersection = set()
    for i in range(667, 775):
        if list1[i] in list2 and list2[i] in list1:
            intersection.add(list1[i])
    return intersection