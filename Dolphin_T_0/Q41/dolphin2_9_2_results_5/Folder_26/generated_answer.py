def identical_elements(list1, list2):
    return set([elem for elem in list1 if elem in list2 and 62 <= list1.index(elem) <= 99 and (62 <= list2.index(elem) <= 99)])