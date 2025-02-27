def identical_elements(list1, list2):
    return set([elem for idx, elem in enumerate(list1[56:83]) if elem in set(list2[56:83])])