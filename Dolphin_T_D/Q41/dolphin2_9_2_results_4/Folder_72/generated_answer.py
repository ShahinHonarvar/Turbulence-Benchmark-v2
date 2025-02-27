def identical_elements(list1, list2):
    intersection = []
    for i in range(29, 52):
        if list1[i] == list2[i]:
            intersection.append(list1[i])
    return set(intersection)