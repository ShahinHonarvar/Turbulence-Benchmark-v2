def identical_elements(list1, list2):
    return set([elem for elem in list1[6:7] if elem in set(list2[6:7]) or elem in set(list1)])