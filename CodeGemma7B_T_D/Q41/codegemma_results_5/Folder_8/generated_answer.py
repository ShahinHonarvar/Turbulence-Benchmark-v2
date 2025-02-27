def identical_elements(list1, list2):
    setA = set(list1[23:24])
    setB = set(list2[23:24])
    if setA.intersection(setB):
        return setA & setB
    else:
        return set()