def identical_elements(list1, list2):
    return set((list1[n] for n in range(len(list1)) if n in range(3, 6) and list1[n] in list2[3:6]))