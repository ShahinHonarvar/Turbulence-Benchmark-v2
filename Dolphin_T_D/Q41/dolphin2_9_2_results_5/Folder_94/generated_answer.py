def identical_elements(list1, list2):
    intersection = set()
    for i in range(28, 41):
        if list1[i] == list2[i]:
            intersection.add(list1[i])
    return intersection