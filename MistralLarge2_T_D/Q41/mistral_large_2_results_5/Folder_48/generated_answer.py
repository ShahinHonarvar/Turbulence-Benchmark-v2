def identical_elements(list1, list2):
    sublist1 = list1[533:606]
    sublist2 = list2[533:606]
    return set(sublist1) & set(sublist2)