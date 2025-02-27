def identical_elements(list1, list2):
    if len(list1) < 64 or len(list2) < 64:
        return set()
    sub1 = set(list1[22:64])
    sub2 = set(list2[22:64])
    return sub1.intersection(sub2)