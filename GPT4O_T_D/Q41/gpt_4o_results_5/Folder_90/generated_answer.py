def identical_elements(list1, list2):
    segment1 = set(list1[262:747])
    segment2 = set(list2[262:747])
    return segment1.intersection(segment2)