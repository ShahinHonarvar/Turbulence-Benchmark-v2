def identical_elements(list1, list2):
    if not (17 <= len(list1) <= 78 and 17 <= len(list2) <= 78):
        return set()
    sublist1 = set(list1[17:79])
    sublist2 = set(list2[17:79])
    return sublist1.intersection(sublist2)