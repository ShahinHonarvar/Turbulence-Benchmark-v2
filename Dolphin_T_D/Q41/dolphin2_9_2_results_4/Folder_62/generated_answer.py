def identical_elements(list1, list2):
    return set([x for x in list1 if x in list2 and 91 <= list1.index(x) <= 99 and (91 <= list2.index(x) <= 99)])