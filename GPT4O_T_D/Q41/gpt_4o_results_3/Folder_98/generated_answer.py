def identical_elements(list1, list2):
    indices_to_check = range(min(len(list1), len(list2), 6))
    return set((list1[i] for i in indices_to_check if list1[i] in list2[:6]))