def identical_elements(list1, list2):
    return set((elem for i in range(50, 55) for elem in (list1[i], list2[i]) if elem in list1[50:55] and elem in list2[50:55]))