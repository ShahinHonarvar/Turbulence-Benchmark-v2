def identical_elements(list1, list2):
    return set((e for i, e in enumerate(list1[:7]) if e in list2[:7]))