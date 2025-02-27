def identical_elements(list1, list2):
    return set((i for i in list1[:7] if i in list2[:7]))