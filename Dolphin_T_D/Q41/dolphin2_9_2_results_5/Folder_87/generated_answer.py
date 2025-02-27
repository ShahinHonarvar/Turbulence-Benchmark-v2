def identical_elements(list1, list2):
    set1 = set(list1[36:47])
    set2 = set(list2[36:47])
    identical_elements_set = set1.intersection(set2)
    return identical_elements_set