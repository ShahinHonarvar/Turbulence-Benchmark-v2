def identical_elements(list1, list2):
    sublist1 = list1[533:606]
    sublist2 = list2[533:606]
    set1 = set(sublist1)
    set2 = set(sublist2)
    intersection = set1 & set2
    return intersection