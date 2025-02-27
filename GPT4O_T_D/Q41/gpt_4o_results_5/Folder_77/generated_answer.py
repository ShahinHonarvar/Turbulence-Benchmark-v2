def identical_elements(list1, list2):
    if not (len(list1) > 538 and len(list2) > 538):
        return set()
    return set(list1[527:539]).intersection(list2[527:539])