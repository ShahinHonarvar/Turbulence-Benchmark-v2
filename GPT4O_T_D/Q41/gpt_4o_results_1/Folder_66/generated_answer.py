def identical_elements(list1, list2):
    if len(list1) < 55 or len(list2) < 55:
        return set()
    sublist1 = list1[50:55]
    sublist2 = list2[50:55]
    return set(sublist1).intersection(sublist2)