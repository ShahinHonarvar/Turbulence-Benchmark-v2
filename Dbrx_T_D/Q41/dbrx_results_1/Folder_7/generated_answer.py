def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set((list1[i] for i in range(661, 925) if list1[i] == list2[i]))