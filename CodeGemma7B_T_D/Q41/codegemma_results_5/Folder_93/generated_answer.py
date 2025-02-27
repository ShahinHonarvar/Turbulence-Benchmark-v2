def identical_elements(list1, list2):
    return set((a for a in list1[75:95] for b in list2[75:95] if a == b))