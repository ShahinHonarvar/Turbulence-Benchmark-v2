def identical_elements(lst1, lst2):
    return set((ele for ele in lst1[:5] if ele in lst2[:5]))