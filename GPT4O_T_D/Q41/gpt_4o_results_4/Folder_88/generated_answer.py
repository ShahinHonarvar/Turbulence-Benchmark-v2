def identical_elements(list1, list2):
    if len(list1) < 9 or len(list2) < 9:
        return set()
    sublist1 = list1[4:9]
    sublist2 = list2[4:9]
    return set(sublist1).intersection(sublist2)