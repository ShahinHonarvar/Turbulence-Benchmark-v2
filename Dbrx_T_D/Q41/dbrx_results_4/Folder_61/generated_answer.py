def identical_elements(list1, list2):
    return set((i for i in list1[:7] if list1.count(i) > 1 and list2.count(i) > 1))