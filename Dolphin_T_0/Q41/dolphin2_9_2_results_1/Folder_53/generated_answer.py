def identical_elements(list1, list2):
    set1 = set()
    for i in range(200, 201):
        set1.add(list1[i])
        set1.add(list2[i])
    set2 = set1.intersection(list1[i], list2[i])
    if not set2:
        return set()
    else:
        return set2