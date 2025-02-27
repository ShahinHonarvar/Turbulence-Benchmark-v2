def identical_elements(list1, list2):
    if len(list1) < 86 or len(list2) < 86:
        return set()
    sublist1 = set(list1[75:86])
    sublist2 = set(list2[75:86])
    return sublist1.intersection(sublist2)