def identical_elements(list1, list2):
    sublist1 = set(list1[527:539])
    sublist2 = set(list2[527:539])
    return sublist1.intersection(sublist2)