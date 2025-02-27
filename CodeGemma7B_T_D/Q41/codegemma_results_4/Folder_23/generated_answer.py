def identical_elements(lst1, lst2):
    indices = list(range(52, 72))
    return set((lst1[i] for i in indices if lst2[i] in lst1[i] for i in indices))