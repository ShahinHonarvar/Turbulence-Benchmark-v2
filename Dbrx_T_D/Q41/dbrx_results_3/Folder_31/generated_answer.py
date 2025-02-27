def identical_elements(list1, list2):
    overlap = set()
    if len(list1) != len(list2):
        return overlap
    for i in range(len(list1)):
        if i >= 75 and i <= 88:
            if list1[i] in list2:
                overlap.add(list1[i])
    return overlap