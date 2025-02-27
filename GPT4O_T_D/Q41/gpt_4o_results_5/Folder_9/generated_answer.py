def identical_elements(list1, list2):
    set1 = set(list1[70:201])
    set2 = set(list2[70:201])
    result = set1.intersection(set2)
    return result