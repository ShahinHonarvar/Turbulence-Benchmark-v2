def identical_elements(list1, list2):
    if len(list1) < 60 or len(list2) < 60:
        return set()
    sublist1 = list1[25:60]
    sublist2 = list2[25:60]
    return set(sublist1).intersection(sublist2)