def identical_elements(list1, list2):
    return set((element for i in range(8) if element in list1[i:i + 1] and element in list2[i:i + 1]))