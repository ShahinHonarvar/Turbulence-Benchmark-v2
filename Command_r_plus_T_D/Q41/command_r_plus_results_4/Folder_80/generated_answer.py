def identical_elements(list1: list, list2: list) -> set:
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size.')
    return set(list1[64:67]).intersection(list2[64:67])