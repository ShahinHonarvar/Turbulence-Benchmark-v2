def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size')
    if len(list1) <= 6:
        return set()
    return set(list1[6:]) & set(list2[6:])