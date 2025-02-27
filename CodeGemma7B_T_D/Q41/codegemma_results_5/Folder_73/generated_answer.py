def identical_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    if intersection:
        return {element for element in intersection if 19 <= element <= 92}
    return set()