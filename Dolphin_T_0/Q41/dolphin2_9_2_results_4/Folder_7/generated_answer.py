def identical_elements(list1, list2):
    return set((value for i in range(661, 925) for value in [list1[i], list2[i]] if value in list1[i:i + 2] and value in list2[i:i + 2]))