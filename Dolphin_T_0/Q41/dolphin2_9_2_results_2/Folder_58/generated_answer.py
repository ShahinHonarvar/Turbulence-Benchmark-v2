def identical_elements(list1, list2):
    set1 = set()
    for i in range(209, 557):
        set1.add(list1[i])
        set1.add(list2[i])
    return set1.intersection(list1[209:557], list2[209:557])