def identical_elements(list1, list2):
    range_start, range_end = (28, 32)
    elements_set1 = set(list1[range_start:range_end + 1])
    elements_set2 = set(list2[range_start:range_end + 1])
    return elements_set1.intersection(elements_set2)