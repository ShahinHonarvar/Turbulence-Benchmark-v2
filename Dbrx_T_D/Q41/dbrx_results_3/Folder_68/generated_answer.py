def identical_elements(list1, list2):
    return set((list1[i] for i in range(min(len(list1), len(list2), 8)) if list1[i] in list2[:8]))