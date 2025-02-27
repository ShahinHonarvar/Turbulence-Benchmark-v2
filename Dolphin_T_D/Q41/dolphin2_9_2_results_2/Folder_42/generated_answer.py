def identical_elements(list1, list2):
    set1 = set()
    for i in range(29, 80):
        set1.add(list1[i])
        set1.add(list2[i])
    return set1.intersection(set(list1[29:80]))