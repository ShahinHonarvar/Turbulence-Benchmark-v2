def identical_elements(list1, list2):
    range_start, range_end = (533, 605)
    subset1 = set(list1[range_start:range_end + 1])
    subset2 = set(list2[range_start:range_end + 1])
    return subset1.intersection(subset2)