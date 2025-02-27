def identical_elements(list1, list2):
    return set((a for a, b in zip(list1[75:95], list2[75:95]) if a == b))