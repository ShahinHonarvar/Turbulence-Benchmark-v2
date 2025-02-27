def identical_elements(list1, list2):
    if len(list1) < 79 or len(list2) < 79:
        return set()
    sublist1 = list1[62:79]
    sublist2 = list2[62:79]
    return set(sublist1).intersection(sublist2)