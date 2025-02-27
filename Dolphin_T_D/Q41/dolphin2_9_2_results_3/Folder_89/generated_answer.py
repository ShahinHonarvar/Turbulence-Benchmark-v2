def identical_elements(list1, list2):
    set1 = set()
    set2 = set()
    for i in range(56, 83):
        if i < len(list1):
            set1.add(list1[i])
        if i < len(list2):
            set2.add(list2[i])
    return set1.intersection(set2)