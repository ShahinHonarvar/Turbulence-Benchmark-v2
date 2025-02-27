def identical_elements(list1, list2):
    set1 = set([list1[i] for i in range(62, 100)])
    set2 = set([list2[i] for i in range(62, 100)])
    return set1 & set2