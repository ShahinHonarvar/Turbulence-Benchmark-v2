def identical_elements(list1, list2):
    intersection = set(list1[31:73]) & set(list2[31:73])
    return intersection if intersection else set()