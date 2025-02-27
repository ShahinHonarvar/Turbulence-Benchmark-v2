def identical_elements(list1, list2):
    sublist1 = set(list1[262:747])
    sublist2 = set(list2[262:747])
    return sublist1.intersection(sublist2)