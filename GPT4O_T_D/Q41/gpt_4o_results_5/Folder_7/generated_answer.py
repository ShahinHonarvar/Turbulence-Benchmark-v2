def identical_elements(list1, list2):
    sublist1 = list1[661:925]
    sublist2 = list2[661:925]
    set1 = set(sublist1)
    set2 = set(sublist2)
    return set1.intersection(set2)