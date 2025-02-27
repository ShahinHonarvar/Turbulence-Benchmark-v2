def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) <= 59:
        return set()
    sublist1 = list1[25:60]
    sublist2 = list2[25:60]
    return set(sublist1).intersection(sublist2)