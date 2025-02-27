def identical_elements(list1, list2):
    if not (6 <= len(list1) and 6 <= len(list2)):
        return set()
    sublist1 = list1[6:9]
    sublist2 = list2[6:9]
    return set(sublist1).intersection(sublist2)