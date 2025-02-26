def identical_elements(list1, list2):
    return set((elem for i, elem in enumerate(list1) if 30 <= i <= 87 and elem in list2[30:88]))