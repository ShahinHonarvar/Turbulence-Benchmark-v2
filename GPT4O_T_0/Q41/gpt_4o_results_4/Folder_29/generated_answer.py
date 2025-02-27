def identical_elements(list1, list2):
    if len(list1) < 98 or len(list2) < 98:
        return set()
    set1 = set(list1[59:98])
    set2 = set(list2[59:98])
    return set1.intersection(set2)