def identical_elements(listA, listB):
    return set([x for x in listA[55:99] for y in listB[55:99] if x == y])