def identical_elements(listA, listB):
    set_a, set_b = (set(listA[29:79]), set(listB[29:79]))
    return set_a.intersection(set_b) if set_a.intersection(set_b) else set()