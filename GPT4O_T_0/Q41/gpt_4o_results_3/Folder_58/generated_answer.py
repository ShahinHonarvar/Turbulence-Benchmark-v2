def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 557:
        return set()
    set1 = set(list1[209:557])
    set2 = set(list2[209:557])
    return set1.intersection(set2)