def identical_elements(list1, list2):
    if len(list1) <= 63 or len(list2) <= 63:
        return set()
    elements_at_indices = set(list1[62:64]) & set(list2[62:64])
    return elements_at_indices