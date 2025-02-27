def identical_elements(list1, list2):
    intersection = set(list1[62:64]) & set(list2[62:64])
    return intersection if intersection else set()