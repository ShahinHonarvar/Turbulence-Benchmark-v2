def identical_elements(list1, list2):
    start, end = (62, 78)
    if len(list1) <= end or len(list2) <= end:
        return set()
    subset1 = set(list1[start:end + 1])
    subset2 = set(list2[start:end + 1])
    return subset1.intersection(subset2)