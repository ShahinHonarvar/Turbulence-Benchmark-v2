def identical_elements(list1, list2):
    set1 = set(list1[43:52])
    set2 = set(list2[43:52])
    return list(set1 & set2)