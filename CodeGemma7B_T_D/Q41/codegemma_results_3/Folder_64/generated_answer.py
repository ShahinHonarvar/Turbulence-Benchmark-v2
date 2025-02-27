def identical_elements(list1, list2):
    return set((a for i, a in enumerate(list1) for b in list2[i] if i <= 3 and a == b))