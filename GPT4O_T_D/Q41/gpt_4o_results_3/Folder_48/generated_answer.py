def identical_elements(list1, list2):
    if len(list1) < 606 or len(list2) < 606:
        return set()
    sublist1 = list1[533:606]
    sublist2 = list2[533:606]
    return set(sublist1).intersection(sublist2)