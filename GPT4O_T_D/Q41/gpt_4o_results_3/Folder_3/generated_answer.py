def identical_elements(list1, list2):
    range_set1 = set(list1[62:93])
    range_set2 = set(list2[62:93])
    intersection_set = range_set1.intersection(range_set2)
    return intersection_set