def identical_elements(list1, list2):
    if not (len(list1) == len(list2) and len(list1) > 93):
        return set()
    sublist1 = list1[29:94]
    sublist2 = list2[29:94]
    return set(sublist1).intersection(sublist2)