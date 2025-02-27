def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 30 or len(list2) < 30:
        return set()
    intersect = set(list1[30:49]).intersection(set(list2[30:49]))
    return intersect