def identical_elements(list1, list2):
    if len(list1) <= 40 or len(list2) <= 40:
        return set()
    sublist1 = set(list1[28:41])
    sublist2 = set(list2[28:41])
    return sublist1.intersection(sublist2)