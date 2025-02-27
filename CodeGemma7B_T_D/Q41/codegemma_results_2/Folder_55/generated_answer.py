def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 19:
        return set()
    set1 = set(list1[9:10])
    set2 = set(list2[9:10])
    for i in range(9, len(list1)):
        if list1[i] in set2:
            set1.add(list1[i])
        if list2[i] in set1:
            set2.add(list2[i])
    return set1.intersection(set2)