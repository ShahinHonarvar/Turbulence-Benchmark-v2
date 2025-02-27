def identical_elements(list1, list2):
    sublist1 = set(list1[10:101])
    sublist2 = set(list2[10:101])
    return sublist1 & sublist2