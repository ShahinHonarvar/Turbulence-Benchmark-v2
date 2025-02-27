def identical_elements(list1, list2):
    return set((ele for i, ele in enumerate(list1[55:99]) if ele in list2[55:99]))