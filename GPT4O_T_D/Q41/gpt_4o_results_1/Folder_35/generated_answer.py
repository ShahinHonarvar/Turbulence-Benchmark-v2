def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    range_start, range_end = (30, 48)
    if len(list1) <= range_end:
        return set()
    elements1 = set(list1[range_start:range_end + 1])
    elements2 = set(list2[range_start:range_end + 1])
    return elements1 & elements2