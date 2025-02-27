def identical_elements(list1, list2):
    return set((i for i in range(8) for j in range(8) if list1[i] == list2[j]))