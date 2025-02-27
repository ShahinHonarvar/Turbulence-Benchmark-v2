def identical_elements(list1, list2):
    set1 = set([x for x in list1])
    set2 = set([x for x in list2])
    return set1.intersection(set2)