def identical_elements(list1, list2):
    intersection = []
    for i in range(20, 31):
        if list1[i] in list2:
            intersection.append(list1[i])
    return set(intersection)