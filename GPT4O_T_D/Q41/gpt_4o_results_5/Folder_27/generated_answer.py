def identical_elements(list1, list2):
    if len(list1) < 94 or len(list2) < 94:
        return set()
    sublist1 = list1[66:94]
    sublist2 = list2[66:94]
    return set(sublist1).intersection(sublist2)