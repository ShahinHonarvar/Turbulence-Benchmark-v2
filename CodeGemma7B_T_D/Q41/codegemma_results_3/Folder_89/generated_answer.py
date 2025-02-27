def identical_elements(list1, list2):
    return set((a for a, b in zip(list1[56:83], list2[56:83]) if a == b))