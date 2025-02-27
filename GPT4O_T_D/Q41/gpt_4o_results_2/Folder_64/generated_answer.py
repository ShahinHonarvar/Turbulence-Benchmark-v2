def identical_elements(list1, list2):
    sublist1 = set(list1[:4])
    sublist2 = set(list2[:4])
    return sublist1 & sublist2