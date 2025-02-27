def identical_elements(list1, list2):
    sublist1 = set(list1[29:80])
    sublist2 = set(list2[29:80])
    return sublist1.intersection(sublist2)