def identical_elements(list1, list2):
    overlapping_elements = set(list1[60:200]) & set(list2[60:200])
    return overlapping_elements