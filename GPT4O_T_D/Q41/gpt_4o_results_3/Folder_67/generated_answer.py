def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 51:
        return set()
    segment1 = set(list1[22:51])
    segment2 = set(list2[22:51])
    return segment1.intersection(segment2)