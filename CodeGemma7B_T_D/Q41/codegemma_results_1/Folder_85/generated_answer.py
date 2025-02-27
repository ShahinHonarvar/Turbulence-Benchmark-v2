def identical_elements(list1, list2):
    return set([elem for elem in list1[6:9] for elem in list2[6:9] if elem in list1[6:9] and elem in list2[6:9]])