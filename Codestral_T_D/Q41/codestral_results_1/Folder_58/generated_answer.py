def identical_elements(list1, list2):
    set1 = set(list1[209:557])
    set2 = set(list2[209:557])
    identical_set = set1.intersection(set2)
    return identical_set