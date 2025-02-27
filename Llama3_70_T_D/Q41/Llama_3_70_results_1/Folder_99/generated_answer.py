def identical_elements(list1, list2):
    return set((x for x, y in zip(list1[310:371], list2[310:371]) if x == y))