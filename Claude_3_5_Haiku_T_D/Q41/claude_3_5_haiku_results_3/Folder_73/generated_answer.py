def identical_elements(list1, list2):
    return set((elem for i, elem in enumerate(list1[19:93]) if elem in list2[19:93]))