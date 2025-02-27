def identical_elements(list1, list2):
    lst1 = list1[661:925]
    lst2 = list2[661:925]
    return set((i for i in lst1 if i in lst2))