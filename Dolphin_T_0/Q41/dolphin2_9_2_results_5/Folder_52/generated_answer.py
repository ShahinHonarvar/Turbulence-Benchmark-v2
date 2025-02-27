def identical_elements(list1, list2):
    set1 = set([x for x in list1[28:39]])
    set2 = set([x for x in list2[28:39]])
    return set1 & set2