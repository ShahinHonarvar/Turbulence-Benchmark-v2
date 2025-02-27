def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    intersect = set(list1[40:81]) & set(list2[40:81])
    return intersect