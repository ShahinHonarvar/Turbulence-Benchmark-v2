def identical_elements(list1, list2):
    if len(list1) < 64 or len(list2) < 64:
        return set()
    sublist1 = set(list1[22:64])
    sublist2 = set(list2[22:64])
    return sublist1.intersection(sublist2)