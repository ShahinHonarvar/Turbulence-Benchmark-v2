def identical_elements(list1, list2):
    return set([x for x in list1[14:65] if list1.count(x) >= 1 and list2.count(x) >= 1])