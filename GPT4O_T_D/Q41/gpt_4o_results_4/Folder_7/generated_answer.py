def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    sublist1 = set(list1[661:925])
    sublist2 = set(list2[661:925])
    return sublist1.intersection(sublist2)