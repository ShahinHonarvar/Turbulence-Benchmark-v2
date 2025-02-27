def identical_elements(list1, list2):
    return set((list1[i] for i in range(len(list1)) if i >= 27 and i <= 55 and (list1[i] in list2[i]) and (list2[i] in list1[i])))