def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 988:
        return set()
    return set(list1[686:988]).intersection(list2[686:988])