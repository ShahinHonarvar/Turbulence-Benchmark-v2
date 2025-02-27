def identical_elements(list1, list2):
    intersection = set(list1[5:8]) & set(list2[5:8])
    return intersection if intersection else set()