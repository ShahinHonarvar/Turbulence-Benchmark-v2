def identical_elements(list1, list2):
    if len(list1) <= 987 or len(list2) <= 987:
        return set()
    sublist1 = set(list1[686:988])
    sublist2 = set(list2[686:988])
    return sublist1.intersection(sublist2)