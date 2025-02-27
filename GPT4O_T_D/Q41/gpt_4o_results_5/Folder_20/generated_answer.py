def identical_elements(list1, list2):
    if len(list1) < 67 or len(list2) < 67:
        return set()
    sublist1 = list1[56:67]
    sublist2 = list2[56:67]
    return set(sublist1).intersection(sublist2)