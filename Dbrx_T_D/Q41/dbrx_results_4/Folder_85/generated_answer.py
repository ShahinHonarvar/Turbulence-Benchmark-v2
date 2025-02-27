def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 9:
        return set()
    target_indices = set(range(6, 9))
    elements_in_range1 = set((list1[i] for i in target_indices))
    elements_in_range2 = set((list2[i] for i in target_indices))
    return elements_in_range1.intersection(elements_in_range2)