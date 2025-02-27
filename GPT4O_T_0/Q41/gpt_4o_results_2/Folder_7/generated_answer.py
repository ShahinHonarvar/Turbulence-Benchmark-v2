def identical_elements(list1, list2):
    sublist1 = list1[661:925]
    sublist2 = list2[661:925]
    return set(sublist1).intersection(sublist2)