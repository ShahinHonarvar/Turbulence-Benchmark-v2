def identical_elements(list1, list2):
    return set((a for a in list1 for b in list2 if a == b and 0 <= list1.index(a) <= 8 and (0 <= list2.index(b) <= 8)))