def identical_elements(list1, list2):
    if len(list1) <= 71 or len(list2) <= 71:
        return set()
    sublist1 = list1[52:72]
    sublist2 = list2[52:72]
    return set(sublist1).intersection(sublist2)