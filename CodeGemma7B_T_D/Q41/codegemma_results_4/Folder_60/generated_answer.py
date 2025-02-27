def identical_elements(list1, list2):
    return set((a for a in list1[75:86] for b in list2[75:86] if a == b))