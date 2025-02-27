def identical_elements(list1, list2):
    if len(list1) < 96 or len(list2) < 96:
        return set()
    subset1 = set(list1[74:96])
    subset2 = set(list2[74:96])
    return subset1.intersection(subset2)