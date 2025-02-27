def identical_elements(list1, list2):
    if len(list1) < 39 or len(list2) < 39:
        return set()
    sublist1 = list1[28:39]
    sublist2 = list2[28:39]
    return set(sublist1) & set(sublist2)