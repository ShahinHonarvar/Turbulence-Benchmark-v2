def identical_elements(list1, list2):
    range_start = 70
    range_end = 85
    if len(list1) < range_end or len(list2) < range_end:
        return set()
    return set(list1[range_start:range_end]) & set(list2[range_start:range_end])