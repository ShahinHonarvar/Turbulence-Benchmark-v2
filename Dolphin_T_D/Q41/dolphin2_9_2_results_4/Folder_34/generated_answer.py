def identical_elements(list1, list2):
    set1 = set([el for el in list1[60:201]])
    set2 = set([el for el in list2[60:201]])
    return set1.intersection(set2)