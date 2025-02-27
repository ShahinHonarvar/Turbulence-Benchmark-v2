def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set(list1[10:67]).intersection(set(list2[10:67]))