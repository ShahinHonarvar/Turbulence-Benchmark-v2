def identical_elements(list1, list2):
    set1 = set(list1[14:65])
    set2 = set(list2[14:65])
    result = set1.intersection(set2)
    return result