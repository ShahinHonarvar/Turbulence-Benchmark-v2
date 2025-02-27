def identical_elements(list1, list2):
    if len(list1) < 93 or len(list2) < 93:
        return set()
    sublist1 = list1[19:93]
    sublist2 = list2[19:93]
    return set(sublist1) & set(sublist2)