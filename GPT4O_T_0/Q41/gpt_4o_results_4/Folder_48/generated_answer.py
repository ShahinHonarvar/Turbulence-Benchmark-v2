def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 606:
        return set()
    return set(list1[533:606]).intersection(list2[533:606])