def identical_elements(list1, list2):
    set1 = set()
    set2 = set()
    for i in range(70, 201):
        if i < len(list1):
            set1.add(list1[i])
            set2.add(list2[i])
    return set1.intersection(set2)