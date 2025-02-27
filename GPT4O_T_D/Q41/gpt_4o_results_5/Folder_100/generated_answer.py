def identical_elements(list1, list2):
    if len(list1) < 69 or len(list2) < 69:
        return set()
    sublist1 = set(list1[42:69])
    sublist2 = set(list2[42:69])
    return sublist1.intersection(sublist2)