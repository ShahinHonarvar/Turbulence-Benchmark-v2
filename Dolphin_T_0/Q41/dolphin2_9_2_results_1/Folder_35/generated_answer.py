def identical_elements(list1, list2):
    set1 = set(list1[min(30, len(list1)):min(49, len(list1)) + 1])
    set2 = set(list2[min(30, len(list2)):min(49, len(list2)) + 1])
    return set1 & set2