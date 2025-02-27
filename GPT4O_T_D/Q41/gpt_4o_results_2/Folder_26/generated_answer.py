def identical_elements(list1, list2):
    if len(list1) < 100 or len(list2) < 100:
        return set()
    set1 = set(list1[62:100])
    set2 = set(list2[62:100])
    result = set1.intersection(set2)
    return result