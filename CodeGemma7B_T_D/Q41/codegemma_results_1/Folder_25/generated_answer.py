def identical_elements(list1, list2):
    return set((a for a, b in zip(list1[29:94], list2[29:94]) if a == b))