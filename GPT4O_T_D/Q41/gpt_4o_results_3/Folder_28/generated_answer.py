def identical_elements(list1, list2):
    if len(list1) < 64 or len(list2) < 64:
        return set()
    set1 = set(list1[62:64])
    set2 = set(list2[62:64])
    return set1.intersection(set2)