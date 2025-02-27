def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    set1 = set([x for i, x in enumerate(list1) if 661 <= i <= 924])
    set2 = set([x for i, x in enumerate(list2) if 661 <= i <= 924])
    return set1.intersection(set2)