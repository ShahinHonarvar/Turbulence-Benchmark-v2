def identical_elements(list1, list2):
    return set((t for t in [[l1, l2] for l1 in list1[31:72] for l2 in list2[31:72]] if l1 == l2))