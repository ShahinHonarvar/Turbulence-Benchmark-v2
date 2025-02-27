def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 539:
        return set()
    segment1 = set(list1[527:539])
    segment2 = set(list2[527:539])
    return segment1.intersection(segment2)