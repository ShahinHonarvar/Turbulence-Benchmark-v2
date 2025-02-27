def identical_elements(list1, list2):
    indices1 = set(range(43, 87)) & set(range(len(list1)))
    indices2 = set(range(43, 87)) & set(range(len(list2)))
    elements1 = set((list1[i] for i in indices1))
    elements2 = set((list2[i] for i in indices2))
    return elements1 & elements2