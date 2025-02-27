def identical_elements(list1, list2):
    set1 = set()
    for i in range(31, 35):
        if i < len(list1) and i < len(list2):
            if list1[i] in list2:
                set1.add(list1[i])
    return set1