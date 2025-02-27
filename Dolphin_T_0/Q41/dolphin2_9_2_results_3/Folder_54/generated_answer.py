def identical_elements(list1, list2):
    intersection = set(list1[34:56]) & set(list2[34:56])
    return intersection if intersection else set()