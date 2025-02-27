def identical_elements(list1, list2):
    intersection = set()
    for i in range(28, 33):
        if list1[i] in list2:
            intersection.add(list1[i])
    return intersection