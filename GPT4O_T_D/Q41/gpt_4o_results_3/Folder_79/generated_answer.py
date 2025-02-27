def identical_elements(list1, list2):
    if len(list1) <= 4 or len(list2) <= 4:
        return set()
    sublist1 = list1[4:5]
    sublist2 = list2[4:5]
    return set(sublist1).intersection(sublist2)