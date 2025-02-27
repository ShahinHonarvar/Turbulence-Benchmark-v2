def identical_elements(list1, list2):
    same_elements = set()
    for i in range(74, 96):
        if list1[i] == list2[i]:
            same_elements.add(list1[i])
    return same_elements