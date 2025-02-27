def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    intersection = set(list1[75:86]).intersection(set(list2[75:86]))
    return intersection if len(intersection) > 0 else set()