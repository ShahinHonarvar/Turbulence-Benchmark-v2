def identical_elements(list1, list2):
    set1 = set([el for el in list1[527:539]])
    set2 = set([el for el in list2[527:539]])
    return set1.intersection(set2)