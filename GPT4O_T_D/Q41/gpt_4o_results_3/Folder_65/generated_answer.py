def identical_elements(list1, list2):
    sublist1 = list1[56:99]
    sublist2 = list2[56:99]
    return set(sublist1).intersection(sublist2)