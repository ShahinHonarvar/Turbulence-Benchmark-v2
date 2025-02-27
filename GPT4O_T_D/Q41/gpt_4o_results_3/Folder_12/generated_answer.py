def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must have the same length.')
    range_start = 14
    range_end = 64
    sublist1 = list1[range_start:range_end + 1]
    sublist2 = list2[range_start:range_end + 1]
    return set(sublist1) & set(sublist2)