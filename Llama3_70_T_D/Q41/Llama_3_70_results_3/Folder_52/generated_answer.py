def identical_elements(list1, list2):
    return set((x for x, y in zip(list1[28:39], list2[28:39]) if x == y))