def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 88:
        return set()
    sublist1 = set(list1[25:88])
    sublist2 = set(list2[25:88])
    return sublist1.intersection(sublist2)