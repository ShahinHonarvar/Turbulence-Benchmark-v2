def identical_elements(list1, list2):
    return set((elem for elem in set(list1[4:9] + list2[4:9]) if elem in list1[4:9] and elem in list2[4:9]))