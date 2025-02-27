def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    indices = range(22, 89)
    return set((el for i, el in enumerate(list1) if i in indices and el in list2))