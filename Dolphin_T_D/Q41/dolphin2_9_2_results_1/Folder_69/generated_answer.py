def identical_elements(lst1, lst2):
    return set((lst1[i] for i in range(32, 36) if lst1[i] in lst2[32:36]))