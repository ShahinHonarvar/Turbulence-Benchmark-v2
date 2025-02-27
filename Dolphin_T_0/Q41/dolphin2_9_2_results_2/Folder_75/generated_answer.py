def identical_elements(list1, list2):
    set_elements = set(list1[56:58] + list2[56:58])
    return set_elements.intersection(list1[56:58], list2[56:58])