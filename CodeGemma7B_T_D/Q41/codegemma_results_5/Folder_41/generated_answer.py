def identical_elements(listA, listB):
    if len(listA) != len(listB):
        return set()
    else:
        setA = set(listA[6:13])
        setB = set(listB[6:13])
        return setA.intersection(setB)