def identical_elements(list1, list2):
    sublist1 = list1[26:53]
    sublist2 = list2[26:53]
    return set(sublist1) & set(sublist2)