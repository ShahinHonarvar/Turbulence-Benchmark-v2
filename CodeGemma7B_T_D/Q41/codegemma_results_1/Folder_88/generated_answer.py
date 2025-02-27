def identical_elements(list1, list2):
    return set((a for a in range(4, 9) for b in range(4, 9) if list1[a] == list2[b]))