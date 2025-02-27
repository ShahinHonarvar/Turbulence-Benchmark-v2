def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 539:
        return set()
    return set(list1[527:539]).intersection(list2[527:539])