def identical_elements(list1, list2):
    if len(list1) <= 97 or len(list2) <= 97:
        return set()
    subset1 = set(list1[59:98])
    subset2 = set(list2[59:98])
    return subset1.intersection(subset2)