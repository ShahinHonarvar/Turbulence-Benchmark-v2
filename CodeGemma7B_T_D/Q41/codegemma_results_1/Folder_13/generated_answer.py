def identical_elements(listA, listB):
    set1 = set(listA[25:88])
    set2 = set(listB[25:88])
    return set1.intersection(set2)