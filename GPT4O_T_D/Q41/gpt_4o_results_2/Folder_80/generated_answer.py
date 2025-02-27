def identical_elements(list1, list2):
    range_start = 64
    range_end = 66
    if len(list1) <= range_end or len(list2) <= range_end:
        return set()
    elements_list1 = set(list1[range_start:range_end + 1])
    elements_list2 = set(list2[range_start:range_end + 1])
    return elements_list1.intersection(elements_list2)