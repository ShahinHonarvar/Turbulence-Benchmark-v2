def identical_elements(list1, list2):
    if len(list1) < 77 or len(list2) < 77:
        return set()
    sublist1 = list1[37:77]
    sublist2 = list2[37:77]
    return set(sublist1).intersection(sublist2)