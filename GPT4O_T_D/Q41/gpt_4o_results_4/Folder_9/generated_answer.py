def identical_elements(list1, list2):
    segment1 = set(list1[70:201])
    segment2 = set(list2[70:201])
    return segment1.intersection(segment2)