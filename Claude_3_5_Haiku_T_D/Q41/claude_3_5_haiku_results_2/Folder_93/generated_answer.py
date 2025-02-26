def identical_elements(list1, list2):
    return set((elem for i, elem in enumerate(list1[75:95]) if elem in list2[75:95]))