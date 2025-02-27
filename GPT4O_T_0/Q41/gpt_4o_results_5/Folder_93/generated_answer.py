def identical_elements(list1, list2):
    if len(list1) < 95 or len(list2) < 95:
        return set()
    sublist1 = list1[75:95]
    sublist2 = list2[75:95]
    return set(sublist1).intersection(sublist2)