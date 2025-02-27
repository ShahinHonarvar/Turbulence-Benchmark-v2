def identical_elements(list1, list2):
    range_start = 639
    range_end = 975
    set1 = set(list1[range_start:range_end + 1])
    set2 = set(list2[range_start:range_end + 1])
    return set1.intersection(set2)