def identical_elements(list1, list2):
    return set((list1[i] for i in range(62, 93) if list1[i] == list2[i])) & set(list1[62:93]) & set(list2[62:93])