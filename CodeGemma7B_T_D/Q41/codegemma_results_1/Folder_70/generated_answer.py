def identical_elements(list_one, list_two):
    common_elements = set((l1 for l1, l2 in zip(list_one[28:33], list_two[28:33]) if l1 == l2))
    return common_elements or set()