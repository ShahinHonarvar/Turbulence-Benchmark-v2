def identical_elements(list1, list2):
    elements = set((a for a, b in zip(list1[10:67], list2[10:67]) if a == b))
    return elements if elements else set()