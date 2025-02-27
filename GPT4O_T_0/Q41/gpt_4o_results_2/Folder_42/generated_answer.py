def identical_elements(list1, list2):
    if len(list1) < 80 or len(list2) < 80:
        return set()
    sublist1 = list1[29:80]
    sublist2 = list2[29:80]
    return set(sublist1).intersection(sublist2)