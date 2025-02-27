def identical_elements(list1, list2):
    set1 = set()
    for i in range(34, 56):
        if i < len(list1) and i < len(list2):
            set1.add(list1[i])
            set1.add(list2[i])
    set2 = set()
    for i in list1:
        if i in set1:
            set2.add(i)
    return set2