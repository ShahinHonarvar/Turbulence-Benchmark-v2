def identical_elements(list1, list2):
    set1 = set()
    set2 = set()
    for i in list1[40:201]:
        set1.add(i)
    for i in list2[40:201]:
        set2.add(i)
    return set1.intersection(set2)