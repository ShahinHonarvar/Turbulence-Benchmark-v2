def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size.')
    start, end = (17, 78)
    set1 = set(list1[start:end + 1])
    set2 = set(list2[start:end + 1])
    return set1.intersection(set2)