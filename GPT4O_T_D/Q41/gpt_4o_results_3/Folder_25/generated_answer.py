def identical_elements(list1, list2):
    start, end = (29, 93)
    sublist1 = set(list1[start:end + 1])
    sublist2 = set(list2[start:end + 1])
    return sublist1.intersection(sublist2)